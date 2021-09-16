import os
import argparse
import json
import logging

# 왜 안되는지 모르겠서영
# from attrdic import AttrDict

class AttrDict(dict):

    def __getattr__(self, attr):
        return self.__getitem__(attr)

    def __setattr__(self, attr, value):
        return self.__setitem__(attr, value)

    def __delattr__(self, attr):
        return self.__delitem__(attr)

logger = logging.getLogger(__name__)

def main(config_file):
    with open(config_file) as f:
        args = AttrDict(json.load(f))
    logger.info("Training/evaluation parameters {}".format(args))



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c", "--config_file", dest="config_file", default="configs/AlexNet.json", type=str, help="Path of configuration file",
    )
    parser = parser.parse_args()
    main(parser.config_file)