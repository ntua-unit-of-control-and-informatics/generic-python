from base64 import b64encode, b64decode
import pickle


def decode(rawModel):
    model = b64decode(rawModel)
    p_mod = pickle.loads(model)
    return p_mod
    # raw = b64encode(p_mod)
    # raw_model = raw.decode(self.ENCODING)
    # ENCODING = 'utf-8'