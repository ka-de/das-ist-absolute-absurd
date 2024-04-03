// Components
class PositionComponent {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }
}

class RenderComponent {
    constructor(color, radius) {
        this.color = color;
        this.radius = radius;
    }
}

class TreasureComponent {
    constructor(x, y, radius, color) {
        this.x = x;
        this.y = y;
        this.radius = radius;
        this.color = color;
        this.isOpened = false;
    }
}

// Entity
class Entity {
    constructor() {
        this.components = {};
    }

    addComponent(component) {
        this.components[component.constructor.name] = component;
    }

    getComponent(componentName) {
        return this.components[componentName];
    }
}

// Systems
class RenderSystem {
    constructor(ctx) {
        this.ctx = ctx;
    }

    render(entity) {
        const position = entity.getComponent('PositionComponent');
        const render = entity.getComponent('RenderComponent');
        const treasure = entity.getComponent('TreasureComponent');

        if (position && render) {
            this.ctx.beginPath();
            this.ctx.arc(position.x, position.y, render.radius, 0, Math.PI * 2);
            this.ctx.fillStyle = render.color;
            this.ctx.fill();
            this.ctx.closePath();
            
            if (treasure && treasure.isOpened) {
                // Render an opened chest if it has been opened
                this.ctx.fillStyle = 'green';
                this.ctx.fillRect(position.x - render.radius, position.y - render.radius, render.radius * 2, render.radius * 2);
            }
        }
    }
}

// Function to generate random item
function getRandomItem() {
    const commonItems = ['gold', 'silver', 'gems'];
    const rareItems = ['diamond', 'ruby', 'emerald', 'sapphire'];
    const equippableWeapons = Object.values(equippableItems.weapon);
    const equippableArmors = Object.values(equippableItems.armor);

    // Set probability for rare items (10% chance)
    const rareProbability = 0.1;

    // Generate a random number between 0 and 1
    const randomNum = Math.random();

    if (randomNum < rareProbability) {
        // Return a random rare item
        const randomIndex = Math.floor(Math.random() * rareItems.length);
        return rareItems[randomIndex];
    } else {
        // Return a random common item or equippable item
        const allItems = [...commonItems, ...equippableWeapons, ...equippableArmors];
        const randomIndex = Math.floor(Math.random() * allItems.length);
        return allItems[randomIndex];
    }
}

function updateHealthBarUI() {
    const healthBar = document.getElementById('health');
    const playerHealth = document.getElementById('player-health');
    const maxHealth = 100; // Assuming maximum health is 100 for now
    const playerCurrentHealth = player.health;
    const healthPercentage = (playerCurrentHealth / maxHealth) * 100;
    healthBar.style.width = healthPercentage + '%';
    playerHealth.innerText = 'Health: ' + playerCurrentHealth + ' / ' + maxHealth;
}

// Define equippable items
const equippableItems = {
    weapon: {
        sword: { type: 'weapon', name: 'Sword', damage: 10 },
        axe: { type: 'weapon', name: 'Axe', damage: 15 },
        bow: { type: 'weapon', name: 'Bow', damage: 12 }
    },
    armor: {
        helmet: { type: 'armor', name: 'Helmet', defense: 5 },
        chestplate: { type: 'armor', name: 'Chestplate', defense: 10 },
        shield: { type: 'armor', name: 'Shield', defense: 8 }
    }
};

// Player's equipped items
let equippedItems = {
    weapon: null,
    armor: null
};

// Function to equip an item
function equipItem(item) {
    if (item.type === 'weapon') {
        equippedItems.weapon = item;
        console.log(`Equipped ${item.name}`);
    } else if (item.type === 'armor') {
        equippedItems.armor = item;
        console.log(`Equipped ${item.name}`);
    }
}

// Function to unequip an item
function unequipItem(type) {
    if (type === 'weapon') {
        equippedItems.weapon = null;
        console.log('Unequipped weapon');
    } else if (type === 'armor') {
        equippedItems.armor = null;
        console.log('Unequipped armor');
    }
}

// Function to get player's total damage
function getPlayerTotalDamage() {
    let totalDamage = 0;
    if (equippedItems.weapon) {
        totalDamage += equippedItems.weapon.damage;
    }
    return totalDamage;
}

// Function to get player's total defense
function getPlayerTotalDefense() {
    let totalDefense = 0;
    if (equippedItems.armor) {
        totalDefense += equippedItems.armor.defense;
    }
    return totalDefense;
}

// Create entities for treasure chests
const treasureChestEntities = treasureChests.map(chest => {
    const entity = new Entity();
    entity.addComponent(new PositionComponent(chest.x, chest.y));
    entity.addComponent(new RenderComponent(chest.color, chest.radius));
    entity.addComponent(new TreasureComponent(chest.x, chest.y, chest.radius, chest.color));
    return entity;
});

// Create a render system instance
const renderSystem = new RenderSystem(ctx);

// Render the player
renderSystem.render(player);

// Render each treasure chest
treasureChestEntities.forEach(entity => {
    renderSystem.render(entity);
});

// Main function to run the simulation
function main(playerLuck) {
    // Initialize canvas and context
    const canvas = document.getElementById('canvas');
    const ctx = canvas.getContext('2d');

    // Player properties
    const player = {
        x: canvas.width / 2,
        y: canvas.height / 2,
        radius: 10,
        color: 'blue',
        speed: 5,
        health: 100 // Initial health
    };

    // Number of attempts to open the treasure chest
    const totalAttempts = 5;

    // Number of successful attempts needed for a rare item
    const successfulAttempts = 3;

    // Simulate opening the treasure chest
    const successful = openTreasureChest(playerLuck, totalAttempts, successfulAttempts);

    // Update health bar UI
    updateHealthBarUI(player);

    // Display the outcome
    if (successful) {
        console.log("Congratulations! You found a rare item in the treasure chest.");
    } else {
        console.log("Better luck next time. No rare item found in the treasure chest.");
    }
}

// Run the main function with a specified player luck (for testing purposes)
const playerLuck = 50; // Set player's luck here
main(playerLuck);
