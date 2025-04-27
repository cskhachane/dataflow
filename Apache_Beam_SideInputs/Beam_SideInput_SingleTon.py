import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(['--runner=DirectRunner'])

stopwords = "the","and","is"

def run():
    with beam.Pipeline(options=options) as pipeline:
        words = pipeline | "createWords" >> beam.Create(['Apache','is','cool','the'])

        stopwords_pcol1 = pipeline | "createstopwords" >> beam.Create([stopwords])

        filtered = words | "filterStopWords" >> beam.Filter(
            lambda word, stop : word.lower() not in stop,
            beam.pvalue.AsSingleton(stopwords_pcol1)
        )

        filtered | "Print" >> beam.Map(print)

        #filtered | 'getOutput' >> beam.io.WriteToText(r'D:\DataFlow\SideInput_SingletonOuput.csv')


if __name__=='__main__':
    run()