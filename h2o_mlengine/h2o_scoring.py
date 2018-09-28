import os
import pandas as pd

class H2O_Scoring():
    """h2o scoring wrapper
        Arguments:
            mojo_path: string path to the MOJO file.
            genmodel_path: string path to the MOJO file.
    """
    def __init__(self, mojo_path=None, genmodel_path=None):
        assert mojo_path != None, "No MOJO path provided"
        assert genmodel_path != None, "No h2o-genmodel path provided"
        self.mojo_path = mojo_path
        self.genmodel_path = genmodel_path

    def _check_file(self, file_path):
        """check if a file exists in the system
            Arguments:
               file_path: string path to the MOJO file.
            Returns:
               bool: True if file exists, false if not
        """
        return True if os.path.isfile(file_path) is True else False

    def _update_input_file(self, input_file, output_file):
        """
            Add the prediction results into the original csv file
            Arguments:
               input_file: string path to the input csv file.
               output_file: string path to the predictions csv file
            Returns:
               updated_file: string path to the file
        """
        original_file = pd.read_csv(input_file)
        predictions = pd.read_csv(output_file)
        predictions = original_file.join(predictions)
        predictions.to_csv(output_file)

    def make_predictions(self, input_file=None, return_as_dataframe=False, output_file=None):
        """Make the predictions given an input_file, if return_as_datagrame is true then
           return a pandas dataframe with the predicions, otherwise store the predicions in the
           output path
            Arguments:
                input_file: string path to the input csv file.
                output_file: string path to the output file.
                return_as_dataframe: bool if True returns a pandas dataframe with the predicions
            Returns:
                results: None if return_as_dataframe is false otherwise pd Dataframe with prediccions
        """
        cmd = "java -cp {0} hex.genmodel.tools.PredictCsv  \
               --header --mojo {1} --input {2} \
               --output {3} --decimal".format(self.genmodel_path,
                                                         self.mojo_path,
                                                         input_file,
                                                         output_file)
        os.system(cmd)
        self._update_input_file(input_file, output_file)
        if return_as_dataframe == True:
            return pd.read_csv(output_file)
        else:
            return None