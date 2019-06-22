class GermanTokenizer(object):
    @staticmethod
    def tokenize(text):
        tokens = []
        for c in text:
            if c.isdigit():
                if len(tokens) == 0:
                    tokens.append(c)
                elif tokens[-1].isdigit() or len(tokens[-1]) > 1:
                    tokens[-1] = tokens[-1] + c
                else:
                    tokens.append(c)
            elif c == ',' or c == '.':
                if len(tokens) > 0 and tokens[-1].isdigit():
                    tokens[-1] = tokens[-1] + c
                else:
                    tokens.append(c)
            else:
                tokens.append(c)
        return tokens
