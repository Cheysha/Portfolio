using System.Collections.ObjectModel;
using Nez;

namespace OverWorld; 


/*
 *    When colliding with this object, it will switch to the scene specified in the SceneName variable
 */

public class SceneTrigger : Component {

    public string SceneName;

    public SceneTrigger(string name) {
        SceneName = name;
    }

    public override void Initialize() {
        Entity.AddComponent(new BoxCollider(16,2));
        base.Initialize();
    }

    public void SwitchScenes() {
        switch (SceneName) {
            case "HouseScene":
                Core.Scene = new HouseScene();
                break;
            case "GameScene":
                Core.Scene = new GameScene();
                break;
        }
    }
}