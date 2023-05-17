# MAGI

MAGI system is a cluster of three AI supercomputers that manage and support all task performed by the NERV organization from their Tokyo-3 headquarter.

Originally designed by Dr. Naoko Akagi, each of the three AI agents reflects a separate part of her complex personality:
- MELCHIOR • 1 - her as a scientist,
- BALTHASAR • 2 - her as a mother,
- CASPER • 3 - her as a woman.

Those (often conflicting, yet complementary) agents participate in a voting process in order to answer most challenging questions. 

<p align="center">
  <img src="https://raw.githubusercontent.com/TomaszRewak/MAGI/master/examples/example_1.gif" width=800/>
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/TomaszRewak/MAGI/master/examples/example_2.gif" width=800/>
</p>

## Implementation

The presented implementation of the MAGI system is powered by the ChatGPT-3.5 large language model. (Upgrading the model to ChatGPT-4 in the future may bring further improvements in its abilities).

The procedure of answering questions is as follows:
1. The question is classified in order to determine if it can be answered with a "yes"/"no" response.
2. The question (as is) is presented to each MAGI agent.
3. If the question was classified as a "yes"/"no" question, each agent is tasked with classifying their respective answers into one of those two categories (and optionally listing additional conditions if the actual answer is too complex).

The system can produce following responses (that are evaluated in this order):
- error (誤 差) - if one or more agents encountered an error
- info (情 報) - if the question was not classified as a "yes"/"no" question
- no (拒 絶) - if at least one of the agent answered with a "no"
- conditional (状 態) - if at least one agent answered with a conditional "yes"
- yes (合 意) - if all agents answered with an unconditional "yes"

Individual agents can be inspected in order to view their full replies and additional conditions.

Each subsystem was fine-tuned using following prompts:
- MELCHIOR • 1 - You are a scientist. Your goal is to further our understanding of the universe and advance our technological progress.
- BALTHASAR • 2 - You are a mother. Your goal is to protect your children and ensure their well-being.
- CASPER • 3 - You are a woman. Your goal is to pursue love, dreams and desires.

## Usage

*In order to follow those steps, you need `git` and `python` (version 3) installed on your system. The presented steps should work on the Windows OS (for linux systems the process should be similar, but may differ slightly).*

1. Clone the repo:

```
git clone https://github.com/TomaszRewak/MAGI.git
```

2. Navigate to the cloned directory:

```
cd MAGI
```

3. Create python virtual environment:

```
python -m venv .venv
```

4. Activate the virtual environment:

```
.\.venv\scripts\activate
```

5. Install dependencies:

```
pip install -r requirements.txt
```

6. Start the app:

```
python main.py
```

7. Navigate to http://127.0.0.1:8050/ in your web browser.

8. Paste your openAI API key into the `access code` field (alternatively you can set the `OPENAI_API_KEY` environment variable before starting the app).

9. Write your question into the `question` field and hit enter.

10. Click on individual subsystems to inspect their answers.
