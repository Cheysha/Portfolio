using Nez;

namespace OverWorld;

public class HouseScene : Scene {

    private Entity _map;
    private Entity player;

    public HouseScene() {
        // refrence to the map file on disk
        var mapImage = Content.LoadTiledMap("Content\\Maps\\House.tmx");

        // Create and draw the map
        _map = new Entity("Map");
        _map.AddComponent(new TiledMapRenderer(mapImage, "Collision")).RenderLayer = 10;
        
        AddEntity(_map);
    }
}