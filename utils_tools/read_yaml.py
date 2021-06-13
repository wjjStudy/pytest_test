# coding:utf-8

import yaml

def readYaml():
    with open("../data/config.yaml") as f:
        info = yaml.load(f,Loader=yaml.FullLoader)
        print(info)
        # print(type(dbinfo))
        return info


if __name__ == '__main__':
    readYaml()
