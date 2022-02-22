import shlex


def is_pattern_valid(single_command, msg_content: str):

    m_splitted = shlex.split(msg_content)

    if msg_content.startswith(single_command.keyword) and len(m_splitted) > single_command.count_aparams:
        # Pattern is valid
        m_splitted.pop(0)
        # Get alone params
        alone_params = []
        for i in range(single_command.count_aparams):
            alone_params.append(m_splitted.pop(0))
        # Get keyword Params
        keyword_params = {}
        while len(m_splitted) != 0:
            for commandArgument in single_command.allowed_args:
                keyword_value_pair = commandArgument.extract_argument_from_text(m_splitted)
                if keyword_value_pair is not None:
                    keyword_params[keyword_value_pair[0]] = keyword_value_pair[1]
                    break
            else:
                return None

        return {
            "aparams": alone_params,
            "kparams": keyword_params
        }