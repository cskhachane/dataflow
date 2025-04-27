import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(['--runner=DirectRunner'])


def run():

    stopwords_list = ["the","and","is"]

    with beam.Pipeline(options=options) as pipeline:
        words = pipeline | "createWords" >> beam.Create(['Apache','is','cool','the'])

        stopwords_list = pipeline | "createstopwords" >> beam.Create(stopwords_list)

        filtered = words | "filterStopWords" >> beam.Filter(
            lambda word, stop : word.lower() not in stop,
            beam.pvalue.AsList(stopwords_list)
        )

        filtered | "Print" >> beam.Map(print)

if __name__=='__main__':
    run()