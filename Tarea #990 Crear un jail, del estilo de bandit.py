import ast
import json
@AUTHOR OVANDO CUPUL JOSE DOMINGO

class BanditJail:
    def _init_(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def process_file(self, filename):
        with open(filename, 'r') as f:
            content = f.read()
        tree = ast.parse(content)
        self.check_tree(tree)

    def check_tree(self, tree):
        for node in ast.walk(tree):
            if isinstance(node, ast.Call):
                func_name = node.func.id
                if func_name in ['open', 'socket']:
                    arg_values = [arg.s for arg in node.args]
                    if any([isinstance(arg_value, str) and arg_value.startswith('%') for arg_value in arg_values]):
                        self.report_violation(f'Possible SQL injection vulnerability in {func_name} call')

                elif func_name == 'subprocess':
                    args = [arg.s for arg in node.args]
                    if any([arg.startswith('shell=True') for arg in args]):
                        self.report_violation(f'Possible shell command injection vulnerability in {func_name} call')

    def report_violation(self, message):
        print(message)

jail = BanditJail()
jail.add_rule('sql_injection')
jail.add_rule('shell_command_injection')

jail.process_file('example.py')
