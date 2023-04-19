using Microsoft.Xna.Framework;
using Nez;

namespace OverWorld;

/*
 *     Dealing with the player, creating and adding to scene
 *    This is a singleton class, so it can be accessed from anywhere
 */

public class PlayerManager : GlobalManager {

    public Entity player;
    public Vector2 pos;
    
    public PlayerManager() : base() {
        // create player
        player = new Entity("player"){Transform = { Position = new Vector2(200,300)}};
        player.AddComponent<Player>();
    }
    public void AddPlayer(Scene scene) {
        //put player in scene
        scene.AddEntity(player);
    }
}