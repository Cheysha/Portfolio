using Nez;

namespace OverWorld; 

/*
 * This class is responsible for managing the scenes in the game.
 * It is a singleton class, so it can be accessed from anywhere in the game.
 * called when the game starts, and when the player hit a scentrigger.
 */

public class SceneManager : GlobalManager {

    public GameScene gameScene;
    public HouseScene houseScene;
    
    public SceneManager() {
        // list of scenes
        gameScene = new GameScene();
        houseScene = new HouseScene();
    }

    public override void OnEnabled() {
        SetScene(gameScene);
        base.OnEnabled();
    }

    public void SetScene(Scene scene) {
        Core.Scene = scene;
        Core.GetGlobalManager<PlayerManager>().AddPlayer(scene);
        
    }
}