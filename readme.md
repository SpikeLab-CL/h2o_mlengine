## Making h2o batch predictions on Google ML Engine

###Requirements

After training your model, export the `MOJO` and `h2o_genmodel.jar` and save them in Google Cloud Storage.

###Usage

For running on Google ML Engine, launch the following command

```
gcloud ml-engine jobs submit training JOB_NAME \
        --module-name=h2o_mlengine.main \
        --package-path h2o_mlengine/ \
        --region=us-east1 \
        --staging-bucket=gs://project-bucket \
        --scale-tier=BASIC \
        --runtime-version=1.9 \
        -- \
        --mojo_path gs://path/to/mojo.zip \
        --genmodel_path gs://path/to/h2o-genmodel.jar \
        --input_file gs://path/to/input.csv \
        --output_dir gs://bucket/ \
        --output_name output_name.csv
```

For running on your local computer, go to the `h2o_mlengine` folder and lauch:
```
python main.py --mojo_path gs://path/to/mojo.zip --genmodel_path gs://path/to/h2o-genmodel.jar --input_file gs://path/to/input.csv --output_dir gs://bucket/ --output_name output_name.csv
```