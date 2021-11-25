# # NEON AI (TM) SOFTWARE, Software Development Kit & Application Development System
# # All trademark and other rights reserved by their respective owners
# # Copyright 2008-2021 Neongecko.com Inc.
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
# 3. Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from this
#    software without specific prior written permission.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR
# CONTRIBUTORS  BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA,
# OR PROFITS;  OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE,  EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

# pip install simple_NER
# it's here mainly to test that a bad module does not cause failure
# might be useful to tag entities in the future
# check https://github.com/OpenJarbas/simple_NER
from neon_transformers import UtteranceTransformer
import requests
from neon_transformers.tasks import UtteranceTask


class NeuralCoreferenceDemo(UtteranceTransformer):
    task = UtteranceTask.COREFERENCE_RESOLUTION

    def __init__(self, name="neuralcoref_demo", priority=5):
        super().__init__(name, priority)

    @staticmethod
    def solve_corefs(text, lang="en-us"):
        try:
            params = {"text": text}
            r = requests.get("https://coref.huggingface.co/coref",
                             params=params).json()
            return r["corefResText"] or text
        except Exception as e:
            return text

    def transform(self, utterances, context=None):
        context = context or {}
        lang = context.get("lang", "en-us")
        # replace coreferences
        solved = [self.solve_corefs(utt, lang) for utt in utterances]
        solved = [u for u in solved if u not in utterances]
        # return augmented utterances
        return solved + utterances, {}



