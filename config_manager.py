"""
Enhanced Configuration Manager for Costa Farms Sourcing Tool
Includes advanced settings, validation, and team collaboration features
"""

import json
import os
import shutil
import logging
from datetime import datetime
from typing import Dict, List, Optional, Any
from tkinter import filedialog, messagebox
from pathlib import Path
import hashlib

logger = logging.getLogger(__name__)

CONFIG_FILE = "config.json"
BACKUP_DIR = "config_backups"
TEAM_SETTINGS_FILE = "team_settings.json"


class ConfigManager:
    """Enhanced configuration management with validation and team features"""
    
    def __init__(self):
        self.config_file = CONFIG_FILE
        self.backup_dir = BACKUP_DIR
        self.team_settings_file = TEAM_SETTINGS_FILE
        
        # Ensure backup directory exists
        os.makedirs(self.backup_dir, exist_ok=True)
        
        # Load or create config
        self.config = self.load_config()
        self.team_settings = self.load_team_settings()
    
    def load_config(self) -> Dict:
        """Load configuration with validation and migration"""
        if not os.path.exists(self.config_file):
            return self.create_default_config()
        
        try:
            with open(self.config_file, "r") as f:
                config = json.load(f)
            
            # Migrate old configs to new format
            config = self.migrate_config(config)
            
            # Validate configuration
            if self.validate_config(config):
                return config
            else:
                logger.warning("Invalid configuration, using defaults")
                return self.create_default_config()
                
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            messagebox.showerror(
                "Configuration Error",
                "Configuration file corrupted. Creating new configuration."
            )
            return self.create_default_config()
    
    def create_default_config(self) -> Dict:
        """Create comprehensive default configuration"""
        default_config = {
            # Core settings
            "hist_file": "",
            "output_folder": "",
            
            # Advanced settings
            "analysis_settings": {
                "baseline_months": 12,
                "default_track_months": 12,
                "min_savings_threshold": 100,  # Minimum savings to report
                "confidence_threshold": 70,    # Data quality threshold
                "enable_advanced_analytics": True,
                "refresh_excel_connections": False,
                "auto_backup": True
            },
            
            # Email settings for automated reports
            "email_settings": {
                "enabled": False,
                "smtp_server": "",
                "smtp_port": 587,
                "sender_email": "",
                "use_tls": True,
                "recipients": []
            },
            
            # Formatting preferences
            "formatting": {
                "use_costa_branding": True,
                "add_charts": True,
                "add_conditional_formatting": True,
                "currency_symbol": "$",
                "decimal_places": 2
            },
            
            # Data validation rules
            "validation_rules": {
                "max_price_change_pct": 50,  # Flag changes > 50%
                "min_baseline_records": 3,    # Minimum records for baseline
                "outlier_detection": True,
                "outlier_threshold_std": 3    # Standard deviations for outliers
            },
            
            # User preferences
            "user_preferences": {
                "theme": "costa_green",
                "auto_save_projects": True,
                "confirm_before_run": True,
                "show_tips": True,
                "recent_projects": [],
                "favorite_products": []
            },
            
            # Team collaboration
            "team_settings": {
                "share_folder": "",
                "team_name": "",
                "user_name": os.environ.get("USERNAME", "User"),
                "user_role": "Analyst"
            },
            
            # Metadata
            "metadata": {
                "version": "2.0.0",
                "last_updated": datetime.now().isoformat(),
                "config_id": self.generate_config_id()
            }
        }
        
        self.save_config(default_config)
        return default_config
    
    def migrate_config(self, config: Dict) -> Dict:
        """Migrate old configuration format to new structure"""
        # Check if migration needed (old format only has basic fields)
        if "analysis_settings" not in config:
            logger.info("Migrating configuration to new format")
            
            # Backup old config
            self.backup_config(config, "pre_migration")
            
            # Create new config with old values
            new_config = self.create_default_config()
            new_config["hist_file"] = config.get("hist_file", "")
            new_config["output_folder"] = config.get("output_folder", "")
            
            # Preserve any custom settings
            for key, value in config.items():
                if key not in ["hist_file", "output_folder"]:
                    new_config["legacy_settings"] = config
                    break
            
            return new_config
        
        return config
    
    def validate_config(self, config: Dict) -> bool:
        """Validate configuration structure and values"""
        required_keys = ["hist_file", "output_folder", "analysis_settings"]
        
        # Check required keys
        for key in required_keys:
            if key not in config:
                logger.error(f"Missing required configuration key: {key}")
                return False
        
        # Validate file paths if set
        if config.get("hist_file"):
            if not os.path.exists(config["hist_file"]):
                logger.warning(f"Historical file not found: {config['hist_file']}")
                # Don't fail validation, just warn
        
        if config.get("output_folder"):
            if not os.path.exists(config["output_folder"]):
                logger.warning(f"Output folder not found: {config['output_folder']}")
                # Try to create it
                try:
                    os.makedirs(config["output_folder"], exist_ok=True)
                except Exception as e:
                    logger.error(f"Could not create output folder: {e}")
        
        return True
    
    def save_config(self, config: Dict = None) -> bool:
        """Save configuration with backup"""
        if config is None:
            config = self.config
        
        try:
            # Create backup if auto_backup enabled
            if config.get("analysis_settings", {}).get("auto_backup", True):
                self.backup_config(config)
            
            # Update metadata
            config["metadata"]["last_updated"] = datetime.now().isoformat()
            
            # Save configuration
            with open(self.config_file, "w") as f:
                json.dump(config, f, indent=4)
            
            self.config = config
            logger.info("Configuration saved successfully")
            return True
            
        except Exception as e:
            logger.error(f"Failed to save configuration: {e}")
            messagebox.showerror("Save Error", f"Could not save configuration:\n{str(e)}")
            return False
    
    def backup_config(self, config: Dict, suffix: str = None) -> bool:
        """Create backup of configuration"""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            suffix_str = f"_{suffix}" if suffix else ""
            backup_file = os.path.join(
                self.backup_dir,
                f"config_backup_{timestamp}{suffix_str}.json"
            )
            
            with open(backup_file, "w") as f:
                json.dump(config, f, indent=4)
            
            # Clean old backups (keep last 10)
            self.cleanup_old_backups()
            
            logger.info(f"Configuration backed up to {backup_file}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to backup configuration: {e}")
            return False
    
    def cleanup_old_backups(self, keep_count: int = 10):
        """Remove old backup files, keeping only recent ones"""
        try:
            backup_files = sorted(
                Path(self.backup_dir).glob("config_backup_*.json"),
                key=os.path.getmtime,
                reverse=True
            )
            
            for backup_file in backup_files[keep_count:]:
                os.remove(backup_file)
                logger.debug(f"Removed old backup: {backup_file}")
                
        except Exception as e:
            logger.warning(f"Could not cleanup backups: {e}")
    
    def restore_backup(self, backup_file: str = None) -> bool:
        """Restore configuration from backup"""
        try:
            if not backup_file:
                # Get most recent backup
                backup_files = sorted(
                    Path(self.backup_dir).glob("config_backup_*.json"),
                    key=os.path.getmtime,
                    reverse=True
                )
                
                if not backup_files:
                    messagebox.showinfo("No Backups", "No backup files found.")
                    return False
                
                backup_file = str(backup_files[0])
            
            with open(backup_file, "r") as f:
                config = json.load(f)
            
            # Validate before restoring
            if self.validate_config(config):
                self.config = config
                self.save_config(config)
                messagebox.showinfo(
                    "Restore Complete",
                    f"Configuration restored from:\n{os.path.basename(backup_file)}"
                )
                return True
            else:
                messagebox.showerror("Restore Failed", "Backup file is invalid.")
                return False
                
        except Exception as e:
            logger.error(f"Failed to restore backup: {e}")
            messagebox.showerror("Restore Error", f"Could not restore backup:\n{str(e)}")
            return False
    
    def generate_config_id(self) -> str:
        """Generate unique configuration ID"""
        unique_str = f"{datetime.now().isoformat()}_{os.environ.get('COMPUTERNAME', 'unknown')}"
        return hashlib.md5(unique_str.encode()).hexdigest()[:8]
    
    # Team collaboration features
    def load_team_settings(self) -> Dict:
        """Load team-wide settings from shared location"""
        try:
            # First check if team share folder is configured
            share_folder = self.config.get("team_settings", {}).get("share_folder", "")
            
            if share_folder and os.path.exists(share_folder):
                team_config_path = os.path.join(share_folder, self.team_settings_file)
                
                if os.path.exists(team_config_path):
                    with open(team_config_path, "r") as f:
                        return json.load(f)
            
            # Return default team settings
            return {
                "shared_products": [],
                "vendor_database": {},
                "price_benchmarks": {},
                "team_projects": [],
                "last_sync": None
            }
            
        except Exception as e:
            logger.warning(f"Could not load team settings: {e}")
            return {}
    
    def sync_team_settings(self) -> bool:
        """Synchronize settings with team share"""
        try:
            share_folder = self.config.get("team_settings", {}).get("share_folder", "")
            
            if not share_folder or not os.path.exists(share_folder):
                messagebox.showwarning(
                    "No Team Share",
                    "Please configure team share folder in settings."
                )
                return False
            
            # Save current team settings
            team_config_path = os.path.join(share_folder, self.team_settings_file)
            
            # Merge with existing team settings
            existing_settings = {}
            if os.path.exists(team_config_path):
                with open(team_config_path, "r") as f:
                    existing_settings = json.load(f)
            
            # Update with local changes
            self.team_settings["last_sync"] = datetime.now().isoformat()
            self.team_settings["sync_user"] = self.config["team_settings"]["user_name"]
            
            # Save merged settings
            with open(team_config_path, "w") as f:
                json.dump(self.team_settings, f, indent=4)
            
            messagebox.showinfo("Sync Complete", "Team settings synchronized successfully.")
            return True
            
        except Exception as e:
            logger.error(f"Failed to sync team settings: {e}")
            messagebox.showerror("Sync Error", f"Could not sync settings:\n{str(e)}")
            return False
    
    # Settings update methods
    def update_setting(self, category: str, key: str, value: Any) -> bool:
        """Update a specific setting"""
        try:
            if category in self.config:
                self.config[category][key] = value
                return self.save_config()
            else:
                logger.error(f"Unknown setting category: {category}")
                return False
        except Exception as e:
            logger.error(f"Failed to update setting: {e}")
            return False
    
    def get_setting(self, category: str, key: str, default: Any = None) -> Any:
        """Get a specific setting value"""
        return self.config.get(category, {}).get(key, default)
    
    def reset_to_defaults(self) -> bool:
        """Reset configuration to defaults"""
        if messagebox.askyesno(
            "Reset Configuration",
            "This will reset all settings to defaults.\n\n"
            "Your current configuration will be backed up.\n\n"
            "Continue?"
        ):
            # Backup current config
            self.backup_config(self.config, "before_reset")
            
            # Create new default config
            self.config = self.create_default_config()
            
            messagebox.showinfo("Reset Complete", "Configuration reset to defaults.")
            return True
        
        return False


# Legacy function compatibility
def load_config() -> Dict:
    """Load configuration (legacy compatibility)"""
    manager = ConfigManager()
    return manager.config


def save_config(config: Dict) -> bool:
    """Save configuration (legacy compatibility)"""
    manager = ConfigManager()
    manager.config = config
    return manager.save_config()


def select_hist_file(config: Dict) -> Dict:
    """Prompt user to select HistoricalData.xlsx file"""
    path = filedialog.askopenfilename(
        title="Select Historical Data File",
        filetypes=[
            ("Excel Files", "*.xlsx;*.xls;*.xlsm"),
            ("All Files", "*.*")
        ]
    )
    
    if path:
        config["hist_file"] = path
        
        # Auto-detect if it's a Power Query enabled file
        if path.endswith(".xlsm") or "query" in path.lower():
            config["analysis_settings"]["refresh_excel_connections"] = True
            messagebox.showinfo(
                "Power Query Detected",
                "This appears to be a Power Query enabled file.\n"
                "Excel connections will be refreshed before analysis."
            )
        
        save_config(config)
        messagebox.showinfo("Saved", f"Historical Data file set to:\n{path}")
    
    return config


def select_output_folder(config: Dict) -> Dict:
    """Prompt user to select output folder"""
    path = filedialog.askdirectory(title="Select Output Folder")
    
    if path:
        config["output_folder"] = path
        
        # Create subdirectories for organization
        subdirs = ["reports", "archives", "exports", "charts"]
        for subdir in subdirs:
            os.makedirs(os.path.join(path, subdir), exist_ok=True)
        
        save_config(config)
        messagebox.showinfo(
            "Saved",
            f"Output folder set to:\n{path}\n\n"
            "Subdirectories created for better organization."
        )
    
    return config


def validate_hist_file(config: Dict) -> bool:
    """Ensure historical data file exists and is valid"""
    hist_path = config.get("hist_file", "")
    
    if not hist_path:
        messagebox.showwarning(
            "Missing File",
            "Please select a Historical Data file in Settings."
        )
        return False
    
    if not os.path.exists(hist_path):
        messagebox.showwarning(
            "File Not Found",
            f"The Historical Data file could not be found:\n{hist_path}\n\n"
            "Please update it in Settings."
        )
        return False
    
    # Validate file is readable
    try:
        import pandas as pd
        test_read = pd.read_excel(hist_path, nrows=5)
        
        # Check for required columns - UPDATED FOR NEW FORMAT
        required_cols = [
            "Sage & SAMII[Product Code]",
            "[SumBase_Unit_Cost]",
            "Sage & SAMII[Receipt Date]"
        ]
        
        missing_cols = [col for col in required_cols if col not in test_read.columns]
        
        if missing_cols:
            messagebox.showerror(
                "Invalid File Format",
                f"The selected file is missing required columns:\n"
                f"{', '.join(missing_cols)}\n\n"
                f"Required columns:\n"
                f"• Sage & SAMII[Product Code]\n"
                f"• [SumBase_Unit_Cost]\n"
                f"• Sage & SAMII[Receipt Date]\n"
                f"• [SumBase_RCVD_QTY]\n"
                f"• Sage & SAMII[Vendor Cleaned]\n\n"
                "Please select a valid Historical Data file."
            )
            return False
        
        logger.info(f"Historical file validated: {hist_path}")
        return True
        
    except Exception as e:
        messagebox.showerror(
            "File Read Error",
            f"Could not read the Historical Data file:\n{str(e)}\n\n"
            "Please ensure the file is not corrupted and is in Excel format."
        )
        return False

def export_config(config: Dict, export_path: str = None) -> bool:
    """Export configuration for sharing with team"""
    try:
        if not export_path:
            export_path = filedialog.asksaveasfilename(
                defaultextension=".json",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                title="Export Configuration"
            )
        
        if export_path:
            # Remove sensitive information
            export_config = config.copy()
            if "email_settings" in export_config:
                export_config["email_settings"]["sender_email"] = ""
                export_config["email_settings"]["smtp_server"] = ""
            
            with open(export_path, "w") as f:
                json.dump(export_config, f, indent=4)
            
            messagebox.showinfo(
                "Export Complete",
                f"Configuration exported to:\n{export_path}"
            )
            return True
        
        return False
        
    except Exception as e:
        logger.error(f"Failed to export configuration: {e}")
        messagebox.showerror("Export Error", f"Could not export:\n{str(e)}")
        return False


def import_config(import_path: str = None) -> Dict:
    """Import configuration from file"""
    try:
        if not import_path:
            import_path = filedialog.askopenfilename(
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
                title="Import Configuration"
            )
        
        if import_path:
            with open(import_path, "r") as f:
                imported_config = json.load(f)
            
            manager = ConfigManager()
            
            # Validate imported config
            if manager.validate_config(imported_config):
                # Preserve local paths
                imported_config["hist_file"] = manager.config.get("hist_file", "")
                imported_config["output_folder"] = manager.config.get("output_folder", "")
                
                # Save imported config
                manager.config = imported_config
                manager.save_config()
                
                messagebox.showinfo(
                    "Import Complete",
                    "Configuration imported successfully.\n"
                    "Local file paths have been preserved."
                )
                return imported_config
            else:
                messagebox.showerror(
                    "Import Failed",
                    "The imported configuration is invalid."
                )
                return manager.config
        
        return load_config()
        
    except Exception as e:
        logger.error(f"Failed to import configuration: {e}")
        messagebox.showerror("Import Error", f"Could not import:\n{str(e)}")
        return load_config()