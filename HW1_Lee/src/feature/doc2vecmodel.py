from gensim.models.doc2vec import Doc2Vec, TaggedDocument

"""
    Helper class to train gensim's implementation of Doc2Vec (Tomas Mikolov and Quoc Le).
"""
class Doc2VecModel:
    def __init__(self, trainDocs, vectorSize, window, minCount, epochs, retrain):
        self.trainDocs = trainDocs
        self.vectorSize = vectorSize
        self.window = window
        self.minCount = minCount
        self.epochs = epochs
        if retrain:
            self.create()
            self.train()
            self.save('./data/doc2vecmodel/doc2vec.model')
        else:
            self.load('./data/doc2vecmodel/doc2vec.model')

    def load(self, fileName):
        self.model = Doc2Vec.load(fileName)

    def create(self):
        self.model = Doc2Vec(
                self.trainDocs, vector_size=self.vectorSize, window=self.window,
                min_count=self.minCount, epochs=self.epochs, workers=4,
                dm=0, dbow_words=0, hs=0, negative=5, sample=1e-4)

    def train(self):
        self.model.train(
                self.trainDocs,
                total_examples=self.model.corpus_count,
                epochs=self.model.epochs)

    def save(self, fileName):
        self.model.save(fileName)

    def vectorizeDocument(self, document):
        return self.model.infer_vector(document)

    def getTrainingVectors(self):
        return self.model.docvecs.vectors_docs

    def findDocTag(self, index):
        return self.model.docvecs.index_to_doctag(index)

    def findDocVec(self, index):
        return self.model.docvecs.doctag_syn0[index]

    def getTaggedDocVec(self, index):
        return (self.findDocVec(index), self.findDocTag(index))
