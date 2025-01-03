# 🦖 Dino AI Game  

**A thrilling AI-powered game where dinos evolve to dodge obstacles and reach high scores!**  
Built with **Python**, **Pygame**, and **NEAT**, this project is a showcase of NeuroEvolution in action.  

![Game Screenshot Placeholder](demo/demo_gif.gif)

---

## 🚀 Features  

✨ **AI Evolution:** Watch dinos learn and improve with each generation.  
🎨 **Customizable Skins:** Choose from a variety of dino skins.  
🌵 **Dynamic Obstacles:** Randomly generated cacti with increasing difficulty.  
📈 **Score Tracking:** Real-time score display with generation stats.  
🧠 **Neural Networks:** Powered by NEAT to create intelligent dino players.  

---

## 🛠️ Prerequisites  

Ensure you have the following installed before starting:  
- **Python 3.8 or higher**  
- **Pygame library**  
- **NEAT-Python library**  

---

## 📥 Installation  

1. Clone the repository:  

   ```bash
   git clone https://github.com/MansurPro/DinoMindEvolution.git
   cd DinoMindEvolution
   ```

2. Install dependencies:  

   ```bash
   pip install pygame neat-python
   ```

3. Place sprite assets in the `sprites/` directory:  
   - `sprites/dino/`  
   - `sprites/cactus/`  
   - `sprites/road.png`  

---

## 🎮 How to Play  

1. Run the game:  

   ```bash
   python main.py
   ```

2. Sit back and watch the AI dinos evolve to avoid obstacles.  

3. Play the game

   ```bash
   python dino_game.py
   ```

---

## ⚙️ Configuration  

The AI configuration is defined in `config-feedforward.txt`. Modify parameters to customize the AI behavior.  

Example:  
```txt
[NEAT]
fitness_criterion     = max
pop_size              = 20
fitness_threshold     = 10000
```

💡 *Tip: Adjust `pop_size` and `fitness_threshold` to balance performance and complexity.*  

---

## 🖼️ Screenshots  

### Main Game  
![Main Game Screenshot](demo/demo_game.gif)  

### Neural Network in Action  
![Neural Network Screenshot](demo/demo_gif.gif) 

---

## 🧠 How It Works  

1. **Initialization:**  
   - Creates a population of dinos, each controlled by a neural network.  

2. **Gameplay Loop:**  
   - Dinos dodge cacti by learning to jump.  
   - Fitness scores improve with survival and penalize unnecessary jumps.  

3. **Evolution:**  
   - NEAT evolves the neural networks, refining dino behavior across generations.  

---

## 🔮 Future Enhancements  

- 🎵 Add sound effects and background music.  
- 🏆 Create a leaderboard for players.  
- 🔍 Visualize neural networks in real time.  
- 🌌 Introduce dynamic backgrounds and weather effects.  

---

## 📝 License  

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 💬 Contact  

👤 **Your Name**  
📧 Email: [mansurbek1203@gmail.com](mailto:mansurbek1203@gmail.com)  
🌐 GitHub: [@MansurPro](https://github.com/MansurPro)  