from falafel.core.plugins import mapper
from falafel.core import MapperOutput
from falafel.core import LogFileOutput


@mapper("rabbitmq_report", ["total_limit"])
def fd_total_limit(context):
    for line in context.content:
        if "file_descriptors" in line and "total_limit" in line:
            line_splits = line.replace("}", "").split(",")
            if len(line_splits) > 3:
                return int(line_splits[2])


@mapper("rabbitmq_users")
class RabbitMQUsers(MapperOutput):

    @staticmethod
    def parse_content(content):
        users_dict = {}
        for line in content[1:-1]:
            line_splits = line.split()
            if len(line_splits) > 1:
                users_dict[line_splits[0]] = line_splits[1][1:-1]
        return users_dict


@mapper("rabbitmq_startup_log")
class RabbitMQStartupLog(LogFileOutput):
    pass
