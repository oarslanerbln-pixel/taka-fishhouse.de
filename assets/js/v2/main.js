import { initUI } from './modules/ui.js';
import { initNavigation } from './modules/navigation.js';
import { initAnimations } from './modules/animations.js';
import { initMenu } from './modules/menu.js';

document.addEventListener('DOMContentLoaded', () => {
    initUI();
    initNavigation();
    initAnimations();
    initMenu();
    
    // Custom cursor was removed as per original file
});
