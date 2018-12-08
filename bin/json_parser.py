#!/usr/bin/env python3
# coding=utf-8
#------------------------------------------------------------------------------
# This class is used to parse the configuration file.
#
#   Input   :   file name.
#   Output  :   dictionary, field's path as key, json's value as value
#               type of values is appropriately set.
#
#   E.g.,
#       dic = {
#             "/legends/title" : "Install or delete security policies",
#             "/legends/legend/loc" :  0,
#             "/legends/legend/prop" : 28,
#             "/legends/xaxis/label" : "Time (million second)",
#             ...
#       }
#
# By shashibici (shashibici@gmail.com)
#   11/02/2015
#------------------------------------------------------------------------------
# This file could be modified and new features could be added if necessary.
#------------------------------------------------------------------------------

import json
import os
import sys

class JsonParserError(Exception):
    """
        Customized Error for JsonParser
    """
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class JsonParser:
    """
        Input   :   file name.
        Output  :   dictionary, field's path as key, json's value as value
                    type of values is appropriately set.

        E.g.,
            dic = {
                "/legends/title" : "Install or delete security policies",
                "/legends/legend/loc" :  0,
                "/legends/legend/prop" : 28,
                "/legends/xaxis/label" : "Time (million second)",
                ...
            }
    """

    def __init__(self, filename):
        self.config_filename = filename
        self.config = {}
        # The output dictionary
        self.output = {}

    def decode_config(self):
        try:
            with open(os.path.join(os.getcwd(), self.config_filename)) as config_file:
                self.config = json.load(config_file)
                self.json_parse(self.config, "")
        except FileNotFoundError:
            raise JsonParserError("At : " + self.__class__.__name__ + ".decode_config: " +
                                  "File not found: " + os.path.join(os.getcwd(), self.config_filename))
            # code after raise is unreachable
        except JsonParserError as jpe:
            raise JsonParserError("At : " + self.__class__.__name__ + ".decode_config: " +
                                  "Parser json file failed: " + jpe.value)
            # code after raise is unreachable
        except ValueError:
            raise JsonParserError("At : " + self.__class__.__name__ + ".decode_config: " +
                                  "Failed to decode json file: " + os.path.join(os.getcwd(), self.config_filename))
            # code after raise is unreachable

    def json_parse_other(self, jobj, path):
        key = path
        # push into self.output dictionary
        self.output[key] = jobj

    def json_parse_object(self, jobj, path):
        for key in jobj:
            self.json_parse(jobj[key], path+"/"+key)

    def json_parse_array(self, jobj, path):
        index = 0
        for element in jobj:
            self.json_parse(element, path+"/"+"["+str(index)+"]")
            index += 1

    def json_parse(self, jobj, path):
        data_type = type(jobj)
        if data_type is dict:
            #        print "object"
            self.json_parse_object(jobj, path)
            return 1
        elif data_type is list:
            #        print "array"
            self.json_parse_array(jobj, path)
            return 2
        elif jobj is None:
            #        print "null"
            raise JsonParserError("None type of json element")
        else:
            #   print   "string"        ->  str
            #   print   "number"        ->  int
            #   print   "real"          ->  float
            #   print   "true/false"    ->  bool
            self.json_parse_other(jobj, path)
            return 0

    def print(self):
        for key, value in self.output.items():
            data_type = type(value)
            if data_type is int:
                print(key+":" + "(int)")
            elif data_type is str:
                print(key+":" + "(str)")
            elif data_type is float:
                print(key+":" + "(float)")
            elif data_type is bool:
                print(key+":" + "(bool)")
            else:
                print(key+":" + "(" + str(type(value)) + ")")
            print(value)
            print("")


# For testing
# if __name__ == '__main__':
#     argc = len(sys.argv)
#     if argc < 2:
#         print("Usage: " + sys.argv[0] + " <arg1> <arg2> [arg3] [arg4] ... ")
#         exit(1)
#     # data file name
#     data = sys.argv[1]
#     # config file name
#     config = sys.argv[2]
#     FCP = JsonParser(config)
#     FCP.decode_config()
#     FCP.print()
