![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)
![tag:healthcare](https://img.shields.io/badge/healthcare-FF5722)


# Ephemeral Bubble Nursing Assistant

## Problem
50% of patients don't understand their medications. Traditional comprehension checks (verbal confirmation) are unreliable.

## Solution
Ephemeral Biosignal Bubbles: 5-30 second clusters of biosignals (pupil dilation, HRV, GSR) that reveal cognitive state. Multi-agent system analyzes these bubbles to detect confusion in real-time.

## Quick Start

### Install
```
pip install -r requirements.txt
```

### Test Demo
```
python test_demo.py
```

### Run All Agents
```
python main.py
```

## Agents

- **Coordinator** (Port 8000) - Chat Protocol interface
  - Address: `agent1qwhdpakl6plmszd73xntzs57d0x6sr7w08kqpsm2f5f9sq34ejuf25jkdh9`

- **Bubble Analyzer** (Port 8002) - Biosignals to comprehension
  - Address: `agent1qt4wdnau7hes8jqyvcgta0m4yev8v53j9dtplagqg7qxs3hd5882u56e63g`

- **Verifier** (Port 8003) - Validates understanding (threshold 0.7)
  - Address: `agent1qf2dxnp70hj7gpmkjapq6f8amqrlg8shnts5zhzvqedv6kw84zspv0685nr`

- **Alert Agent** (Port 8004) - Notifies nurses
  - Address: `agent1q2mvrlgvurq4ertdza0d8j73fulzx3c86pfk5ucqfvtj5uxzgqxmwkg2t2h`

- **Learning Agent** (Port 8005) - Pattern recognition
  - Address: `agent1q02v98pwsugqp96dzhqlrl39g2mx02jlfq8p0l6eeca0w5npcsfjqf0m53r`

## Deployment Status

**Local Testing**: ✅ All agents functional and tested locally

**Agentverse Registration**: ⚠️ Agents configured for mailbox deployment. Registration attempted but encountered Agentverse API errors (500 status) during submission window. Agents are fully functional locally and can be registered post-hackathon when API is stable.

**Agent Addresses** (for future registration):
- Coordinator: `agent1qwhdpakl6plmszd73xntzs57d0x6sr7w08kqpsm2f5f9sq34ejuf25jkdh9`
- Bubble Analyzer: `agent1qt4wdnau7hes8jqyvcgta0m4yev8v53j9dtplagqg7qxs3hd5882u56e63g`
- Verifier: `agent1qf2dxnp70hj7gpmkjapq6f8amqrlg8shnts5zhzvqedv6kw84zspv0685nr`
- Alert Agent: `agent1q2mvrlgvurq4ertdza0d8j73fulzx3c86pfk5ucqfvtj5uxzgqxmwkg2t2h`
- Learning Agent: `agent1q02v98pwsugqp96dzhqlrl39g2mx02jlfq8p0l6eeca0w5npcsfjqf0m53r`

## How It Works

1. Collect 15 biosignal readings (15 seconds)
2. Create ephemeral bubble
3. Calculate comprehension score
4. If < 0.5: Alert nurse
5. If >= 0.7: Understanding verified

## Privacy
- Edge processing only
- Raw biosignals stay on device
- Bubbles auto-delete after analysis
