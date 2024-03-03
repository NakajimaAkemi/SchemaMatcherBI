import babelnet as bn
from babelnet import Language

synsets = bn.get_synsets('home', from_langs=[Language.EN],
                         to_langs=[Language.IT, Language.FR])
for synset in synsets:
    print('Synset ID:', synset.id)