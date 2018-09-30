import argparse
from h2o_scoring import H2O_Scoring
from ml_engine_utils import download_file_from_storage, save_in_gcs
import os

def main(args):
    input_file = download_file_from_storage(args.input_file)
    genmodel_path = download_file_from_storage(args.genmodel_path)
    mojo_path = download_file_from_storage(args.mojo_path)
    output_name = args.output_name
    
    scorer = H2O_Scoring(mojo_path=mojo_path, genmodel_path=genmodel_path)
    scorer.make_predictions(input_file=input_file, output_file=output_name)

    save_in_gcs(output_name, args.output_dir)
    print("Predictions stored at: ",args.output_dir)
    os.remove(input_file)
    os.remove(genmodel_path)
    os.remove(mojo_path)
    os.remove(output_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--mojo_path', type=str, help="path to the MOJO file")
    parser.add_argument('--genmodel_path', type=str, help="path to the h2o_genmodel file")
    parser.add_argument('--input_file', type=str, help="path to the input csv file")
    parser.add_argument('--output_dir', type=str, help="path to the output directory")
    parser.add_argument('--output_name', type=str, help="name of the output name")
    args = parser.parse_args()
    main(args)