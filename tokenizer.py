"""
Stage 1: Byte-Pair Encoding (BPE) tokenizer, built from scratch.

This file is a SCAFFOLD, not a solution. The three public methods below
are the tokenizer's entire contract. Fill in the bodies yourself.

Recap of the mechanism (see Stage 1 theory for the full derivation):
  - Start from raw UTF-8 bytes (0-255) as the base vocabulary. That's
    "byte-level" BPE — text.encode("utf-8") gets you there.
  - TRAIN: repeatedly find the most frequent adjacent pair of token ids
    in the sequence, invent a new token id for it, and replace every
    non-overlapping occurrence, left to right. Do this
    (vocab_size - 256) times. Record each merge, IN ORDER — order
    matters, because a later merge can be built on top of an earlier
    one (recall X = ZY from the worked trace).
  - ENCODE: never re-learn anything. Take new text, turn it into bytes,
    and replay the learned merges in the exact order they were learned.
  - DECODE: reverse the mapping — for each token id, look up which byte
    sequence it stands for, concatenate them all, then
    bytes.decode("utf-8") back to a string.

A note on ties: when two pairs are tied for "most frequent" during
training, which one wins is an implementation choice, not part of the
core algorithm (see the correction in the Stage 1 chat). Pick a rule,
document it in your own docstring, and be consistent. The tests below
only check things that hold true regardless of which tie-break you
pick.

You will need some way to remember, after training, which byte
sequence each token id represents (so decode() can work) - that's
entirely your design call: how you store it internally is up to you.

Useful docs, not solutions:
  - str.encode / bytes.decode: https://docs.python.org/3/library/stdtypes.html#bytes.decode
  - dict.get(key, default): https://docs.python.org/3/library/stdtypes.html#dict.get
  - max(iterable, key=...): https://docs.python.org/3/library/functions.html#max
"""


class BPETokenizer:
    def count_freq(self,li):
        count={}
        for i in range(len(li)-1):
            count[(li[i],li[i+1])]=count.get((li[i],li[i+1]),0)+1
        return count
    def replace(self,id,c,x,y):
        out=[]
        i=0
        while(i<len(id)):
            if i<len(id)-1 and id[i]==x and id[i+1]==y:
                out.append(c)
                i+=2
            else:
                out.append(id[i])
                i+=1
        return out
        
            
    def train(self, text: str, vocab_size: int) -> None:
        """
        Learn a BPE vocabulary from `text`.

        vocab_size must be >= 256 (the base byte vocabulary). The
        number of merges learned is (vocab_size - 256). After this
        call, self should hold whatever state encode()/decode() need
        (learned merges, and a way to map token id -> byte sequence).

        Does not return anything - mutates self.
        """
        self.id=list(text.encode('utf-8'))
        self.merges={}
        self.counter=256
        self.vocab={}
        self.vocab= {i: bytes([i]) for i in range(256)}
        for i in range(vocab_size-256):
          self.adj_freq=self.count_freq(self.id)
          m=max(self.adj_freq,key=self.adj_freq.get)
          x,y=m
          self.id=self.replace(self.id,self.counter,x,y)
          self.merges[(x,y)]=self.counter
          self.vocab[self.counter]= self.vocab[x]+self.vocab[y]
          self.counter+=1
          

            
          
        
            

    def encode(self, text: str) -> list[int]:
        """
        Turn a string into a list of token ids, using the merges
        learned by train(). Must work on text this tokenizer was never
        trained on - including text containing characters that never
        appeared in training (e.g. emoji, accented letters) - because
        byte-level BPE never has an "unknown token" problem. Raises if
        called before train().
        """
        local=list(text.encode('utf-8'))
        for i,j in self.merges:
            local=self.replace(local,self.merges[(i,j)],i,j)
        return local
                    

    def decode(self, ids: list[int]) -> str:
        """
        Turn a list of token ids back into the original string. Must
        satisfy: self.decode(self.encode(x)) == x for any string x,
        once trained. Raises if called before train().
        """
        byte=bytes()
        for i in ids:
            byte+=self.vocab[i]
        return byte.decode('utf-8')
