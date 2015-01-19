from djehuty.command import Command


class MyCommand(Command):
    '''sample command'''

    def get_parser(self, prog_name):
        parser = Command.get_parser(self, prog_name)
        parser.add_argument('-p', '--person',
                            default='doragon',
                            help='person name')
        return parser

    def take_action(self, parsed_args):
        return 'hello {}'.format(parsed_args.person)

class MyCommand2(Command):
    '''sample command2'''

    def get_parser(self, prog_name):
        parser = Command.get_parser(self, prog_name)
        parser.add_argument('-p', '--person',
                            default='doragon',
                            help='person name')
        return parser

    def take_action(self, parsed_args):
        return 'hoge {}'.format(parsed_args.person)
