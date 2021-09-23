import csv
import json
import os

import datasets

_DESCRIPTION = """\
NER final project BERT implementation annotation dataset
"""

_URLs = "https://github.com/suwanii/FYP/tree/main/dataset_conll_bert_ml_iob/"
_TRAINING_FILE = "trainCoNLL_ML.txt"
_DEV_FILE = "devCoNLL_ML.txt"
_TEST_FILE = "testCoNLL_ML.txt"

class jobAnnotationConfig(datasets.BuilderConfig):
    """BuilderConfig for jobAnnotations"""

    def __init__(self, **kwargs):
        """BuilderConfig forjobAnnotations.
        Args:
          **kwargs: keyword arguments forwarded to super.
        """
        super(jobAnnotationConfig, self).__init__(**kwargs)


class jobAnnotation(datasets.GeneratorBasedBuilder):
    """Job Annotation dataset"""
    BUILDER_CONFIGS = [
        Conll2003Config(name="jobAnnotation")
    ]
    
    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                { 
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "ner_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-company",
                                "I-company",
                                "B-post_number",
                                "I-post_number",
                                "B-location",
                                "I-location",
                                "B-no_years",
                                "I-no_years",
                                "B-res_skill",
                                "I-res_skill",
                                "B-title",
                                "I-title",
                                "B-specialization",
                                "I-specialization",
                                "B-qualification",
                                "I-qualification",
                                "B-edu_level",
                                "I-edu_level",
                                "B-seniority",
                                "I-seniority",
                                "B-gender",
                                "I-gender",
                                
                            ]
                        )
                    ),
                }
            ),
            supervised_keys=None,
            homepage=None,
            citation=None,
        )
    
    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls_to_download = {
            "train": f"{_URL}{_TRAINING_FILE}",
            "dev": f"{_URL}{_DEV_FILE}",
            "test": f"{_URL}{_TEST_FILE}",
        }
        downloaded_files = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]}),
        ]
    
    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            tokens = []
            #pos_tags = []
            #chunk_tags = []
            ner_tags = []
            for line in f:
                if line.startswith("-DOCSTART-") or line == "" or line == "\n":
                    if tokens:
                        yield guid, {
                            "id": str(guid),
                            "tokens": tokens,
                            #"pos_tags": pos_tags,
                            #"chunk_tags": chunk_tags,
                            "ner_tags": ner_tags,
                        }
                        guid += 1
                        tokens = []
                        #pos_tags = []
                        #chunk_tags = []
                        ner_tags = []
                else:
                    # conll2003 tokens are space separated
                    splits = line.split(" ")
                    tokens.append(splits[0])
                    #pos_tags.append(splits[1])
                    #chunk_tags.append(splits[2])
                    ner_tags.append(splits[3].rstrip())
            # last example
            yield guid, {
                "id": str(guid),
                "tokens": tokens,
                #"pos_tags": pos_tags,
                #"chunk_tags": chunk_tags,
                "ner_tags": ner_tags,
            }