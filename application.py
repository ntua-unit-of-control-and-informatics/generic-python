import tornado.web
from tornado.ioloop import IOLoop
from source.handlers.regression import LinearModelHandler as linearModelHandler
from source.handlers.tree import TreeModelHandler as treeModelHandler
from source.handlers.ensemble import EnsembleModelHandler as ensembleModelHandler
from source.handlers.svm import SvmModelHandler as svmModelHandler
from source.handlers.clustering import ClusteringModelHandler as clusteringModelHandler
from source.handlers.biclustering import BiclusteringModelHandler as biclusteringModelHandler
from source.handlers.naivebayess import NaiveBayessModelHandler as naiveBayessModelHandler
from source.handlers.nearestneighbours import NearestNeighboursModelHandler as nearestNeighboursModelHandler
from source.handlers.neuralnetwork import NeuralNetworkModelHandler as neuralNetworkModelHandler
from source.handlers.pipeline import PipelineHandler as pipelineHandler
from source.handlers.xgboost import XGBoostHandler as xgBoostHanlder


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hello, world')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/?", MainHandler),
            (r"/predict/linearmodel/?", linearModelHandler),
            (r"/predict/treemodel/?", treeModelHandler),
            (r"/predict/ensemblemodel/?", ensembleModelHandler),
            (r"/predict/svmmodel/?", svmModelHandler),
            (r"/predict/clustemodel/?",clusteringModelHandler),
            (r"/predict/biclustermodel/?", biclusteringModelHandler),
            (r"/predict/naivemodel/?", naiveBayessModelHandler),
            (r"/predict/neighboursmodel/?", nearestNeighboursModelHandler),
            (r"/predict/neuralnetworkmodel/?", neuralNetworkModelHandler),
            (r"/predict/pipeline/?", pipelineHandler),
            (r"/predict/xgboost/?", xgBoostHanlder)
        ]
        tornado.web.Application.__init__(self, handlers)


def main():
    app = Application()
    app.listen(8002)
    print("App Starting")
    IOLoop.instance().start()

if __name__ == '__main__':
    main()
