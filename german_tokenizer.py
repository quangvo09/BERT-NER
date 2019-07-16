class GermanTokenizer(object):
    @staticmethod
    def tokenize(text):
        if str(text).isdigit():
            return [str(text)]

        length = len(text)
        tokens = []
        for i, c in enumerate(text):
            if c.isdigit():
                if len(tokens) == 0:
                    tokens.append(c)
                elif tokens[-1].isdigit() or len(tokens[-1]) > 1:
                    tokens[-1] = tokens[-1] + c
                else:
                    tokens.append(c)
            elif c == ',' or c == '.':
                # previous token isdigit AND next token isdigit
                if len(tokens) > 0 and tokens[-1].isdigit() \
                        and i < length - 1 and text[i+1].isdigit():
                    tokens[-1] = tokens[-1] + c
                else:
                    tokens.append(c)
            else:
                tokens.append(c)
        return tokens
