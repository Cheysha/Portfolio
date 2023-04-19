using Microsoft.Xna.Framework;
using Nez;
using Nez.Tiled;

namespace OverWorld;

/*
 *    This is the main scene in the game, cosists of a map and a player, and is representative of the overworld.
 *    It is loaded when the game starts.
 */

public class GameScene: Scene {
    
    private Entity _map;

    public GameScene() {
        // refrence to the map file on disk
        var mapImage = Content.LoadTiledMap("Content\\Maps\\testRoom.tmx");
        
        // Create and draw the map
        _map = new Entity("Map");
        _map.AddComponent(new TiledMapRenderer(mapImage, "Collision")).RenderLayer = 10;

        populateMap(mapImage);
        
        AddEntity(_map);
    }
    
    // populate the game map with objects found in the map image
    public void populateMap(TmxMap map) {
        foreach (var obj in map.ObjectGroups[0].Objects) {
            
            if (obj.Type == "SceneTrigger") {
                var t = new Entity(){Position = new Vector2(obj.X,obj.Y), Tag = (int)Tags.SceneTrigger};
                var name = obj.Properties["SceneName"];
                t.AddComponent(new SceneTrigger(name));
                AddEntity(t);
            }

            if (obj.Type == "Enemy") {
                var t = new Entity(){Position = new Vector2(obj.X,obj.Y), Tag = (int)Tags.Enemy};
                t.AddComponent<Enemy>();
                AddEntity(t);
            }
        }
    }
    
}