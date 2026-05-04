const fs = require('fs');
const path = require('path');

const sourceDir = path.join(__dirname, 'assets');
const targetDir = path.join(__dirname, '..', 'portfolio_deploy', 'design_system', 'assets');

/**
 * Recursively copies a directory from src to dest.
 */
function copyRecursiveSync(src, dest) {
    const exists = fs.existsSync(src);
    const stats = exists && fs.statSync(src);
    const isDirectory = exists && stats.isDirectory();

    if (isDirectory) {
        if (!fs.existsSync(dest)) {
            fs.mkdirSync(dest, { recursive: true });
        }
        fs.readdirSync(src).forEach(childItemName => {
            copyRecursiveSync(path.join(src, childItemName), path.join(dest, childItemName));
        });
    } else if (exists) {
        fs.copyFileSync(src, dest);
        console.log(`Copied: ${path.basename(src)}`);
    }
}

try {
    console.log(`[SYNC INIT] Mirroring authoritative assets...`);
    console.log(`SOURCE: ${sourceDir}`);
    console.log(`TARGET: ${targetDir}\n`);

    if (!fs.existsSync(sourceDir)) {
        throw new Error(`Source directory ${sourceDir} does not exist.`);
    }

    copyRecursiveSync(sourceDir, targetDir);
    
    console.log('\n[SYNC COMPLETE] Design system assets successfully mirrored to the deployment repository.');
} catch (error) {
    console.error('\n[SYNC FATAL ERROR] Failed to synchronize design system assets.', error);
    process.exit(1);
}
