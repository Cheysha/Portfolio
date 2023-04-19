using System.Collections.Generic;
using Microsoft.Xna.Framework.Graphics;
using Nez;
using Nez.Sprites;
using Nez.Textures;

namespace OverWorld; 

public class Enemy : Component, IUpdatable {

    public Texture2D _texture;
    public List<Sprite> _sprites;
    public Mover _mover;

    public int damage = 3;

    public Enemy() {
        _texture = Core.Content.LoadTexture("Content\\Images\\monsters.png");
        _sprites = Sprite.SpritesFromAtlas(_texture, 16, 16,1); // need to account for margin 
    }
    
    public override void Initialize() {
        Entity.SetTag((int)Tags.Enemy);
        
        _mover = Entity.AddComponent<Mover>();
        
        Entity.AddComponent<SpriteRenderer>().Sprite = _sprites[0];

        Entity.AddComponent<CircleCollider>();
        
        base.Initialize();
    }

    public void Update() {
        
    }
}