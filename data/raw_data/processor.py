class Processor:
    @staticmethod
    def read_json(file_path):
        with open(file_path, encoding='utf-8') as f:
            raw_examples = f.readlines()
        return raw_examples

    def get_examples(self, raw_examples, set_type):
        examples = []
        for raw_example in raw_examples:
          raw_example = eval(raw_example)
          text = raw_example['text']
          event_list = raw_example['event_list']
          for event in event_list:
            labels = []
            event_type = event['event_type']
            arguments = event['arguments']
            for argument in arguments:
              labels.append((event_type+'-'+argument['role'], argument['argument'], argument['argument_start_index']))
              
          print(labels)
          break
        return examples

if __name__ == '__main__':

  processor = Processor()
  raw_examples = processor.read_json('./dev.json')
  examples = processor.get_examples(raw_examples, 'train')