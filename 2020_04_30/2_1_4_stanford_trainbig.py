

from nltk.tokenize.stanford_segmenter import StanfordSegmenter
seg = StanfordSegmenter(path_to_slf4j='/YOUR_PATH/slf4j-api.jar')

seg = StanfordSegmenter()
seg.default_config('zh')
sent = u'这是斯坦福中文分词器测试'
print(seg.segment(sent))
