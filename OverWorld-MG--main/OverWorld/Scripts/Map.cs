using Microsoft.Xna.Framework;
using Nez;
using Nez.Tiled;

namespace OverWorld; 

public class Map : Component, IUpdatable {
    //test for a map component, loads tmx maps from disk aaaaaandd
    public TmxMap mapImage;

    public Map(string name) : base() {
        mapImage = Core.Content.LoadTiledMap("Content\\Maps\\" + name +".tmx");
    }

    public void Update() {
        Entity.AddComponent(new TiledMapRenderer(mapImage, "Collision")).RenderLayer = 10;
    }
    
    
    public void populateMap(TmxMap map) {
        foreach (var obj in map.ObjectGroups[0].Objects) {
            
            if (obj.Type == "SceneTrigger") {
                var t = new Entity(){Position = new Vector2(obj.X,obj.Y), Tag = (int)Tags.SceneTrigger};
                var name = obj.Properties["SceneName"];
                t.AddComponent(new SceneTrigger(name));
                Entity.Scene.AddEntity(t);
            }

            if (obj.Type == "Enemy") {
                var t = new Entity(){Position = new Vector2(obj.X,obj.Y), Tag = (int)Tags.Enemy};
                t.AddComponent<Enemy>();
                Entity.Scene.AddEntity(t);
            }
        }
    }
    
}