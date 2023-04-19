using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Nez;
using OverWorld;

namespace OverWorld;

public enum Tags { NULL, SceneTrigger, Player, Enemy}

public class Game1 : Nez.Core {

    public SceneManager _SceneManager;
    public PlayerManager _PlayerManager;
    
    public Game1() : base() { }//blank constructor

    protected override void Initialize() {
        // nez stuff, BASE SHOULD COME FIRST HERE
        base.Initialize();

        // set up player manager
        _PlayerManager = new PlayerManager();
        RegisterGlobalManager(_PlayerManager);
        
        //set up scene manager, loads scenes
        _SceneManager = new SceneManager();
        RegisterGlobalManager(_SceneManager);
    }
}