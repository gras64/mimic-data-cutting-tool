# Copyright 2017, Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import re
import argparse


class Name:
    def __init__(self):
        # print("importing args: ")
        parser = argparse.ArgumentParser()
        parser.add_argument(
            '--max_char', default="499",
            help='change max characters of sentence')
        parser.add_argument(
            '--file', default="train.text",
            help='file in folder')


        args = parser.parse_args()
        #  print("args: ""\n"+str(args))
        self.check_file(args)



    def check_file(self, args):
        print("check file")
        # self.poodle_loader(lang, args)
        # self.voice_web_loader(lang, args)
        fobj_in = open(args.file)
        fobj_out = open("output-"+args.file, "w")
        fobj_del = open("delete-"+args.file, "w")
        for line in fobj_in:
            number = ""
            number = re.findall(r'(\|\d+\|)', line)
            number = number[0].replace('|', '')
            if int(number) <= int(args.max_char):
                fobj_out.write(str(line))
            else:
                print("delete: "+ line)
                fobj_del.write(str(line))
                continue
        fobj_in.close()
        fobj_out.close()
        fobj_del.close()


if __name__ == "__main__":
    objName = Name()
