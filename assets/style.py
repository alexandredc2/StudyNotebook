from assets.themes import THEMES

def get_theme():
    from assets.themes import ACTIVE_THEME
    return THEMES[ACTIVE_THEME]

def menubar_style():
    t = get_theme()

    return f"""
        QMenuBar#MenuBar{{
            background-color: {t['background_dir']};
            border-bottom: 1px solid {t['border']};
        }}
        
        QPushButton#Frame_MenuBar_Functions_Buttons{{
            background-color: transparent;
        }}
        QPushButton#Frame_MenuBar_Functions_Buttons:hover{{
            border: 1px solid {t['border']};
            border-radius: 5px;
        }}
    """

def directories_style():
    t = get_theme()

    return f"""
        QFrame#Frame_Directories{{
            background-color: {t['background_dir']};
            border-right: 1px solid {t['border']};
        }}
        QFrame#Frame_Directories_Finder_Area{{
            padding: 5px;
            background-color: {t['background_dir_finder']};
            border: 1px solid {t['border']};
            border-radius: 5px;
        }}
        QFrame#Frame_Directories_Folders_Area{{
            
        }}
        
        QLineEdit#Finder_Area_Input{{
            border: none;
            background-color: {t['background_dir_finder']};
            color: {t['color_dflt_directories']};
        }}
        
        QPushButton#Folders_Area_Buttons{{
            padding-left: 5px;
            padding-top: 3px;
            padding-bottom: 3px;
            text-align: left;
            border: none;
            color: {t['color_dflt_directories']};
        }}
        QPushButton#Folders_Area_Buttons:hover{{
            border: 1px solid {t['border']};
            border-radius: 5px;
        }}
        QPushButton#Folders_Area_Buttons:checked{{
            border: 1px solid {t['border']};
            border-radius: 5px;
            color: {t['color_sele_directories']};
            background-color: {t['background_dir_finder']};
        }}
        
    """

def central_style():
    t = get_theme()

    return f"""
        QTabWidget#Tabs_Brainstorms_Area QStackedWidget{{
            background-color: {t['background_central']};
            border: none;
        }}
        QTabWidget#Tabs_Brainstorms_Area {{
            border: none;
        }}
        QTabWidget#Tabs_Brainstorms_Area QTabBar::tab {{
            background-color: {t['background_dir']};
            color: {t['color_dflt_directories']};
            padding: 4px 10px;
            border-right: 1px solid {t['border']};
        }}
        QTabWidget#Tabs_Brainstorms_Area QTabBar::tab:selected {{
            background-color: {t['background_dir_finder']};
            color: {t['color_sele_directories']};
            padding: 4px 10px;
            border-right: 1px solid {t['border']};
        }}
    
        QFrame#Frame_Central_Area{{
            background-color: {t['background_central']};
        }}
        QFrame#Frame_Buttons_Directories{{
            background-color: {t['background_dir']};
        }}
        QFrame#Frame_Canvas{{
            background-color: transparent;
            border: none;
        }}
        
        QSplitter#Splitter_Functions::handle{{
            background-color: {t['border']};
            width: 1px;
            border-right: 1px solid {t['border']};
        }}
        
        QPushButton#Buttons_Functions_Directories_Sorting{{
            background-color: transparent;
        }}
        QPushButton#Buttons_Functions_Directories_Sorting:hover{{
            border: 1px solid {t['border']};
            border-radius: 5px;
        }}
        QPushButton#Buttons_Functions_Directories{{
            background-color: {t['background_btns_dir']};
            text-align: left;
            color: {t['color_btns_dir']};
            border: 1px solid {t['border']};
            border-radius: 5px;
            padding: 5px;
        }}
        QPushButton#Buttons_Functions_Directories:hover{{
            background-color: {t['background_btns_dir_hov']};
        }}
        
        QLabel#Label_Directories_General{{
            color: {t['color_dflt_directories']};
            font-family: "Bahnschrift";
            font-size: 11px;
        }}
        
        QTreeWidget#Trees_Functions_Directories{{
            background-color: transparent;
            padding-top: 5px;
            border: none;
            color: {t['color_dflt_directories']};
        }}
        
        QGraphicsView#BrainstormCanvas{{
            background-color: transparent;
            border: none;
        }}
        
    """