import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

options = PipelineOptions(['--runner=DirectRunner'])


def run():

    with beam.Pipeline(options=options) as pipeline:
        items = pipeline | "createItems" >> beam.Create(['apple','banana','orange','apple','banana','grapes'])

        price_list = [
            ('apple',1.5),
            ('banana',0.75),
            ('orange',1.25)
        ]

        prices = pipeline | 'CreatePrices' >> beam.Create(price_list)

        priced_items = items | "AttachedPrices" >> beam.Map(
            lambda item,price_map : (item, price_map.get(item, 0.0)),
            beam.pvalue.AsDict(prices)
        )

        priced_items | "Print" >> beam.Map(print)

if __name__=='__main__':
    run()