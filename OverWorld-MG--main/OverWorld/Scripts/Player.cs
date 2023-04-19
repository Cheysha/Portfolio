using System.Collections.Generic;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Nez;
using Nez.Sprites;
using Nez.Textures;


namespace OverWorld; 

/*
 *      This is the player class, it is responsible for handling input and moving the player
 *       it is a component that is added to the player entity at startup by the PlayerManager
 *       the player manager will contain
 */

public class Player : Component, IUpdatable {
    private Texture2D _texture;
    private List<Sprite> playerSprites;
    public SpriteRenderer _spriteRenderer;
    
    public Mover _mover;
    public KeyboardState  currentKey;
    
    public Vector2 _faceDirection;
    
    public VirtualIntegerAxis _horizontalAxis;
    public VirtualIntegerAxis _verticalAxis;
    
    public Vector2 _velocity;

    public TextComponent _textComponent; //DEBUG
    public CircleCollider _testcollider;
    
    //down (0,-1)
    //left (-1,0)
    //right (1,0)
    //up (0,1)
    public Player() {
        // DO NOT ADD COMPONENTS HERE! Use Initialize() instead.
        _texture = Core.Content.LoadTexture("Content\\Images\\player2.png");
        playerSprites = Sprite.SpritesFromAtlas(_texture, 16, 16);


        _faceDirection = new Vector2(0, -1);

        // set up our movement VirtualAxis to use the arrow keys
        _horizontalAxis = new VirtualIntegerAxis();
            _horizontalAxis.AddKeyboardKeys(VirtualInput.OverlapBehavior.TakeNewer, Keys.Left, Keys.Right);
        _verticalAxis = new VirtualIntegerAxis();
            _verticalAxis.AddKeyboardKeys(VirtualInput.OverlapBehavior.TakeNewer, Keys.Up, Keys.Down);

    }
    
    public override void Initialize() {
        Entity.SetTag((int)Tags.Player);
        
        _mover = Entity.AddComponent<Mover>();
        
        _spriteRenderer = Entity.AddComponent<SpriteRenderer>();
        
        _spriteRenderer.Sprite = playerSprites[0];

        Entity.AddComponent<CircleCollider>();
        
        _textComponent = Entity.AddComponent<TextComponent>();
        
        _testcollider = Entity.AddComponent<CircleCollider>();
        
       
        
        base.Initialize();
    }
    
    public override void OnEnabled() {
        /*
         *    Adds a camera follow to the player when added to scene. gets a refrence to the map and sets the map size
         *   so the camera can lock to the map
         */
        var _camfollow = Entity.AddComponent(new FollowCamera(Entity,Entity.Scene.Camera));
        var map = Entity.Scene.FindEntity("Map").GetComponent<TiledMapRenderer>();
        
        _camfollow.MapSize = new Vector2(map.Width,map.Height);
        _camfollow.MapLockEnabled = true;
        Entity.Scene.Camera.SetZoom(4);
        
        base.OnEnabled();
    }


    public void Update() {
        handleInput();
        updateCollider();

        _textComponent.Text = _faceDirection.ToString();
    }
    

    public void updateCollider() {
        _testcollider.Radius = 4;
        _testcollider.IsTrigger = true;
        //switch facing direction
        switch (_faceDirection) {
            case (0, -1): // down
                _testcollider.LocalOffset = new Vector2(0, -8);
                break;
            case (0, 1):
                _testcollider.LocalOffset = new Vector2(0, 8);
                break;
            case (-1, 0):
                _testcollider.LocalOffset = new Vector2(-8, 0);
                break;
            case (1, 0):
                _testcollider.LocalOffset = new Vector2(8, 0);
                break;
        }
    }
    public void handleInput() {
        /*
        *  Handles input for the player
        *  Uses the Mover component to move the player
        *  Uses the CollisionResult struct to check for collisions
        */
        
        _velocity = new Vector2(_horizontalAxis, _verticalAxis);
        
        if (_velocity != Vector2.Zero) {
            // not a great way to do this but it works
            if (_velocity == new Vector2(0, 1) || _velocity == new Vector2(0, -1) ||
                _velocity == new Vector2(1, 0) || _velocity == new Vector2(-1, 0)) 
            {
                _faceDirection = _velocity;
                
                if (_velocity == new Vector2(-1,0))
                    _spriteRenderer.FlipX = true;
                else
                    _spriteRenderer.FlipX = false;
            }

            //move the player
            _velocity.Normalize();
            var test = new CollisionResult();
            _mover.Move(_velocity * 100 * Time.DeltaTime,out test);
        }


    }
}