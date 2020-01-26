from config import parse
import commands
import re
import commands

config = parse('config.json')

def run(text):
    if (re.match('close|exit', text, re.IGNORECASE)):
        return 'exit'
    for conf in config:
        matches = re.match(conf['regex'], text, re.IGNORECASE)
        if (matches):
            arg = matches.groups()[-1]
            if (conf['type'] == 'web-click'):
                commands.web_click(arg, conf['url'])
            elif (conf['type'] == 'web'):
                commands.web(arg, conf['url'])
            elif (conf['type'] == 'run'):
                commands.run(arg)
            elif (conf['type'] == 'run-path'):
                commands.run_path(conf['path'])
            elif (conf['type'] == 'command'):
                commands.run_command(conf['command'])
            else:
                print('Unknown type')
            return
        else:
            print('Unknown command')
