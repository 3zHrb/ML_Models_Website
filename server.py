from flask import Flask, request, render_template, url_for, session, jsonify

import pandas as pd
import secrets

from google.cloud import storage
import os
import uuid
import requests
import io

import boto3

import ml_models


s3 = boto3.resource(
    service_name="s3",
    region_name="us-west-2",
    aws_access_key_id=os.getenv("aws_access_key_id"),
    aws_secret_access_key=os.getenv("aws_secret_access_key"),
)

s3_bucketName = "ml-multimodels-users-datasets"

os.environ[
    "GOOGLE_APPLICATION_CREDENTIALS"
] = "/Users/abdulazizalharbi/Downloads/ml-multimodels-5abe861ae81b.json"

bucket_name = "users-datasets"

app = Flask(__name__, template_folder="templates", static_folder="statics")
app.secret_key = secrets.token_hex(16)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/fileSubmitted", methods=["GET", "POST"])
def fileSubmitted():

    print("submit triggered")
    file = request.files["fileCsv"]
    filename = file.filename
    df = pd.read_csv(file)
    session["user_session_key"] = str(uuid.uuid4())

    df.to_csv(
        f'{os.getcwd()}/UsersDataSetsFolder/{session.get("user_session_key")}.csv',
        index=False,
    )

    # CGPClient = storage.Client()
    # bucket = CGPClient.get_bucket(bucket_name)
    # df_csv = df.to_csv(index=False)
    # bolb = bucket.blob(
    #     "{}.csv".format(session.get("user_session_key"))
    # ).upload_from_string(df_csv, "text/csv")

    return render_template(
        "modelSelections.html",
        df=df,
        columns=df.columns.values,
        dfShape=df.shape,
    )


@app.route("/selectedTarget", methods=["POST"])
def selectedTarget():

    modelType = request.form.get("modelType")
    targetColumn = request.form.get("targetColumn")
    scoringMatric = request.form.get("scoringMethodSelect")

    df = pd.read_csv(
        f'{os.getcwd()}/UsersDataSetsFolder/{session.get("user_session_key")}.csv'
    )

    df.dropna(axis=1, inplace=True)

    y = df[targetColumn]
    x = df.drop(targetColumn, axis=1)

    selectedModels = ml_models.models(modelType)

    modelNames = []
    modelAverageScore = []

    for modelName, model in selectedModels.items():
        kfold = ml_models.KFold(n_splits=5)
        cv_result = ml_models.cross_val_score(
            model, x, y, cv=kfold, scoring=scoringMatric
        )
        modelNames.append(modelName)
        modelAverageScore.append(f"{round(cv_result.mean(), 2)}")

    dataFramesFolderPath = os.getcwd() + "/" + "UsersDataSetsFolder"
    os.remove(f"{dataFramesFolderPath}/{session.get('user_session_key')}.csv")

    return render_template(
        "details.html",
        modelType=modelType,
        x=x.columns.values,
        y=y.name,
        modelNames=modelNames,
        modelsLength=len(modelNames),
        modelAverageScore=modelAverageScore,
        scoringMatric=scoringMatric,
    )


if __name__ == "__main__":
    print("Server is on ...")
    app.run(debug=True)
