#!/usr/bin/env python3

import os
import sys
import argparse
import yaml
import tasksdjclient

from lib.helpers import (TDJCHelper, eprint_exception, eprint,
                                   typical_actions_process)
from tasksdjclient.rest import ApiException

yaml.Dumper.ignore_aliases = lambda *args : True
print_traceback = True
print_result = True


def parse_args(argv):
    self_name = os.path.basename(argv[0])
    epilog = '''\
available item-level cmds for bulk actions:
  c    create item
  u    update item
  d    delete item
  n    do nothing'''
    parent_parser = argparse.ArgumentParser(prog=self_name,
                                            description="Client for the tasksdj")
    subparsers = parent_parser.add_subparsers(help="Endpoint groups")
    subparsers.required = True
    subparsers.dest = "group"
    subparser_tasks = subparsers.add_parser("task", help="Utilities for work with Tasks", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_tasks.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_tasks.add_argument("--profile", type=str, help="Config profile")
    subparser_tasks.add_argument("--id", type=str, help="Entity ID")
    subparser_tasks.add_argument("--input-file", type=str, help="Input file")
    subparser_tasks.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    subparser_task_tags = subparsers.add_parser("task-tag", help="Utilities for work with TaskTags", formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)
    subparser_task_tags.add_argument("--action", type=str, help="Possible actions: list | create | get | update | delete | bulk-dump | bulk-upload")
    subparser_task_tags.add_argument("--profile", type=str, help="Config profile")
    subparser_task_tags.add_argument("--id", type=str, help="Entity ID")
    subparser_task_tags.add_argument("--input-file", type=str, help="Input file")
    subparser_task_tags.add_argument("--default-cmd", type=str, help="Default cmd for bulk actions")
    return parent_parser.parse_args(sys.argv[1:])


class TaskClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = TDJCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(tasksdjclient.TasksApi)
        self.base_class = tasksdjclient.Task
        self.list_method = self.api_instance.tasks_list
        self.read_method = self.api_instance.tasks_read
        self.create_method = self.api_instance.tasks_create
        self.update_method = self.api_instance.tasks_update
        self.delete_method = self.api_instance.tasks_delete


class TaskTagClientBase:

    def __init__(self, args):
        self.args = args
        self.helper = TDJCHelper(self.args)
        self.api_instance = self.helper.get_api_instance(tasksdjclient.TaskTagsApi)
        self.base_class = tasksdjclient.TaskTag
        self.list_method = self.api_instance.task_tags_list
        self.read_method = self.api_instance.task_tags_read
        self.create_method = self.api_instance.task_tags_create
        self.update_method = self.api_instance.task_tags_update
        self.delete_method = self.api_instance.task_tags_delete


def main():
    args = parse_args(sys.argv)
    obj = None
    action_process_result = True
    try:
        CB = None
        if args.group == "task":
            CB = TaskClientBase(args)
        elif args.group == "task-tag":
            CB = TaskTagClientBase(args)
        else:
            eprint("Not implemented for group: {}".format(args.group))
            exit(1)
        action_process_result, obj = typical_actions_process(CB)
    except (ApiException, TypeError, OSError, yaml.YAMLError) as e:
        eprint_exception(e, print_traceback=print_traceback)
    if action_process_result == False:
        eprint("Not implemented for action: {}".format(args.action))
        exit(1)
    if print_result and obj is not None:
        yaml.dump(obj, sys.stdout, default_flow_style=False, allow_unicode=True)


if __name__ == "__main__":
    main()