class Pattern:

    def __init__(self, pattern: str):
        self.cmd_names = []
        self.alone_params = []
        self.keyword_params = []
        for pattern_part in pattern.split(' '):
            if pattern_part[0] == '-':
                self.keyword_params.append(pattern_part)
            elif pattern_part[0] == '<':
                self.alone_params.append(pattern_part)
            else:
                self.cmd_names.append(pattern_part)

    def get_pattern_length(self):
        return len(self.cmd_names) + len(self.alone_params) + len(self.keyword_params) * 2


def is_pattern_valid(pattern: str, msg_content: str):
    pattern_obj = Pattern(pattern)
    m_splitted = msg_content.split(' ')

    if pattern_obj.get_pattern_length() != len(m_splitted):
        return None

    for cmd_name in pattern_obj.cmd_names:
        if cmd_name != m_splitted.pop(0):
            return None

    alone_params = {}
    for pattern_alone_param in pattern_obj.alone_params:
        alone_params[pattern_alone_param[1:-1]] = m_splitted.pop(0)

    keyword_params = {}
    for i in range(0, len(m_splitted), 2):
        if m_splitted[i] not in pattern_obj.keyword_params:
            return None
        keyword_params[m_splitted[i][1:]] = m_splitted[i+1]

    return {
        "aparams": alone_params,
        "kparams": keyword_params
    }