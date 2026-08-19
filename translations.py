#coding=utf-8
_languages = ['ja','zh_CN']

_data = {
'vca_sequence': {
	'ja': "シクウェンスを生成します",
	'en': "Generate Sequence",
},
'controllers_simple_tip': {
	'en': "Generate one flex controller per shape key",
},
'vertmap_group_props': {
	'en': "Vertex Maps",
},
'action_selection_filter_tip': {
	'en': "All actions that match the armature's filter term and have users",
},
'curve_poly_side_fwd': {
	'en': "Forward (outer) side",
},
'action_selection_current_tip': {
	'en': "The armature's currently assigned action or NLA tracks",
},
'action_slot_selection_current_tip': {
	'en': "The armature's active action slot",
},
'valvesource_cloth_enable': {
	'en': "Cloth Physics Enable",
},
'subdir_tip': {
	'en': "Optional path relative to scene output folder",
},
'controllers_mode': {
	'ja': "DMXフレックスのコントローラー生成",
	'en': "DMX Flex Controller generation",
},
'scene_export': {
	'ja': "シーンをエクスポート",
	'en': "Scene Export",
},
'shape_stereo_mode_tip': {
	'en': "How stereo split balance should be defined",
},
'bone_rot_legacy': {
	'en': "Legacy rotation",
},
'controllers_advanced_tip': {
	'en': "Insert the flex controllers of an existing DMX file",
},
'triangulate_tip': {
	'en': "Avoids concave DMX faces, which are not supported by Source",
},
'action_filter': {
	'ja': "アクションフィルター",
	'en': "Action Filter",
},
'slot_filter': {
	'en': "Slot Filter",
},
'vca_start_tip': {
	'en': "Scene frame at which to start recording Vertex Animation",
},
'action_filter_tip': {
	'en': "Actions with names matching this filter pattern and which have users will be exported",
},
'slot_filter_tip': {
	'en': "Slots of the assigned Action with names matching this wildcard filter pattern will be exported (blank to export everything)",
},
'shape_stereo_sharpness_tip': {
	'en': "How sharply stereo flex shapes should transition from left to right",
},
'vca_sequence_tip': {
	'en': "On export, generate an animation sequence that drives this Vertex Animation",
},
'shape_stereo_mode': {
	'en': "DMX stereo split mode",
},
'dummy_bone': {
	'en': "Implicit motionless bone",
},
'vca_group_props': {
	'ja': "頂点アニメーション",
	'en': "Vertex Animation",
},
'curve_poly_side': {
	'ja': "ポリゴン生成",
	'en': "Polygon Generation",
},
'group_merge_mech': {
	'ja': "メカニカルな局部は結合",
	'en': "Merge mechanical parts",
},
'action_selection_mode_tip': {
	'en': "How actions are selected for export",
},
'use_scene_export_tip': {
	'en': "Export this item with the scene",
},
'curve_poly_side_back': {
	'en': "Backward (inner) side",
},
'valvesource_vertex_blend': {
	'en': "Blend Params RGB",
},
'bone_rot_legacy_tip': {
	'en': "Remaps the Y axis of bones in this armature to Z, for backwards compatibility with old imports (SMD only)",
},
'controller_source': {
	'ja': "DMXフレックスのコントローラーのソースファイル ",
	'en': "DMX Flex Controller source",
},
'group_suppress_tip': {
	'en': "Export this group's objects individually",
},
'action_selection_current': {
	'ja': "現在 / NLA",
	'en': "Current / NLA",
},
'action_slot_current': {
	'ja': "現在のアクションスロット",
	'en': "Current Action Slot",
},
'shape_stereo_sharpness': {
	'en': "DMX stereo split sharpness",
},
'group_suppress': {
	'ja': "ミュート",
	'en': "Suppress",
},
'shape_stereo_vgroup': {
	'en': "DMX stereo split vertex group",
},
'shape_stereo_vgroup_tip': {
	'en': "The vertex group that defines stereo balance (0=Left, 1=Right)",
},
'controllers_source_tip': {
	'en': "A DMX file (or Text datablock) containing flex controllers",
},
'valvesource_vertex_blend1': {
	'en': "Blend Params Extra (?)",
},
'curve_poly_side_tip': {
	'en': "Determines which side(s) of this curve will generate polygons when exported",
},
'triangulate': {
	'ja': "三角測量",
	'en': "Triangulate",
},
'curve_poly_side_both': {
	'en': "Both sides",
},
'group_merge_mech_tip': {
	'en': "Optimises DMX export of meshes sharing the same parent bone",
},
'action_selection_mode': {
	'en': "Action Selection",
},
'shape_stereo_mode_vgroup': {
	'en': "Use a vertex group to define stereo balance",
},
'vca_end_tip': {
	'en': "Scene frame at which to stop recording Vertex Animation",
},
'valvesource_vertex_paint': {
	'en': "Vertex Paint",
},
'controllers_mode_tip': {
	'en': "How flex controllers are defined",
},
'subdir': {
	'en': "Subfolder",
},
'dummy_bone_tip': {
	'en': "Create a dummy bone for vertices which don't move. Emulates Blender's behaviour in Source, but may break compatibility with existing files (SMD only)",
},
'exportpanel_steam': {
	'ja': "Steam コミュニティ",
	'en': "Steam Community",
},
'exportables_arm_filter_result': {
	'ja': "「{0}」アクション～{1}",
	'en': "\"{0}\" actions ({1})",
},
'exportables_arm_no_slot_filter': {
	'en': "All action slots ({0}) for \"{1}\"",
},
'exportables_flex_count_corrective': {
	'ja': "是正シェイプ：{0}",
	'en': "Corrective Shapes: {0}",
},
'exportables_curve_polyside': {
	'ja': "ポリゴン生成：",
	'en': "Polygon Generation:",
},
'exportmenu_title': {
	'ja': "Source Tools エクスポート",
	'en': "Source Tools Export",
},
'exportables_flex_help': {
	'ja': "フレックス・コントローラーのヘレプ",
	'en': "Flex Controller Help",
},
'exportpanel_title': {
	'ja': "Source Engine エクスポート",
	'en': "Source Engine Export",
},
'exportables_flex_src': {
	'ja': "コントローラーのソースファイル ",
	'en': "Controller Source",
},
'exportmenu_invalid': {
	'en': "Cannot export selection",
},
'qc_title': {
	'ja': "Source Engine QCのコンパイル",
	'en': "Source Engine QC Compiles",
},
'exportables_flex_props': {
	'ja': "フレックスのプロパティ",
	'en': "Flex Properties",
},
'exportables_flex_generate': {
	'ja': "コントローラーを生成します",
	'en': "Generate Controllers",
},
'exportables_flex_split': {
	'ja': "ステレオフルックスの差額：",
	'en': "Stereo Flex Balance:",
},
'exportables_group_mute_suffix': {
	'ja': "(ミユト)",
	'en': "(suppressed)",
},
'exportmenu_scene': {
	'ja': "シーンをエクスポート ({0}つファイル)",
	'en': "Scene export ({0} files)",
},
'exportpanel_dmxver': {
	'ja': "DMXのバージョン：",
	'en': "DMX Version:",
},
'exportpanel_update': {
	'ja': "更新アドオンの確認",
	'en': "Check for updates",
},
'exportables_title': {
	'ja': "Source Engineのエクスポート可能",
	'en': "Source Engine Exportables",
},
'exportables_armature_props': {
	'ja': "アーマティアのプロパティ",
	'en': "Armature Properties ({0})",
},
'qc_bad_enginepath': {
	'ja': "エンジンのパスが無効です",
	'en': "Invalid Engine Path",
},
'qc_invalid_source2': {
	'ja': "Source Engine 2はQCファイルが使いません",
	'en': "QC files do not exist in Source 2",
},
'exportmenu_selected': {
	'en': "Selected objects ({0} files)",
},
'exportables_group_props': {
	'ja': "グループのプロパティ",
	'en': "Group Properties",
},
'qc_no_enginepath': {
	'ja': "エンジンのパスはありません",
	'en': "No Engine Path provided",
},
'exportables_curve_props': {
	'ja': "カーブのプロパティ",
	'en': "Curve Properties",
},
'exportables_flex_count': {
	'ja': "シェイプ：{0}",
	'en': "Shapes: {0}",
},
'activate_dependency_shapes': {
	'en': "Activate dependency shapes",
},
'settings_prop': {
	'en': "Blender Source Tools settings",
},
'bl_info_description': {
	'en': "Importer and exporter for Valve Software's Source Engine. Supports SMD\\VTA, DMX and QC.",
},
'export_menuitem': {
	'en': "Source Engine (.smd, .vta, .dmx)",
},
'help': {
	'ja': "ヘレプ",
	'en': "Help",
},
'bl_info_location': {
	'ja': "ファイル > インポート / エクスポート、シーンのプロパティ",
	'en': "File > Import/Export, Scene properties",
},
'import_menuitem': {
	'en': "Source Engine (.smd, .vta, .dmx, .qc)",
},
'exporter_err_nogroupitems': {
	'en': "Nothing in Group \"{0}\" is enabled for export",
},
'exporter_report_qc': {
	'en': "{0} files exported and {2} QCs compiled ({3}/{4}) in {1} seconds",
},
'exporter_err_relativeunsaved': {
	'en': "Cannot export to a relative path until the blend file has been saved.",
},
'exporter_err_nopolys': {
	'en': "Object {0} has no polygons, skipping",
},
'exporter_err_hidden': {
	'en': "Skipping {0}: object cannot be selected, probably due to being hidden by an animation driver.",
},
'exporter_err_arm_nonuniform': {
	'en': "Armature \"{0}\" has non-uniform scale. Mesh deformation in Source will differ from Blender.",
},
'exporter_err_facesnotex_ormat': {
	'en': "{0} faces on {1} did not have a Material or Texture assigned",
},
'exporter_err_arm_noanims': {
	'en': "Couldn't find any animation for Armature \"{0}\"",
},
'exporter_err_dupeenv_arm': {
	'en': "Armature modifier \"{0}\" found on \"{1}\", which already has a bone parent or constraint. Ignoring.",
},
'exporter_err_bonelimit': {
	'en': "Exported {0} bones, but SMD only supports {1}!",
},
'exporter_err_unmergable': {
	'en': "Skipping vertex animations on Group \"{0}\", which could not be merged into a single DMX object due to its envelope. To fix this, either ensure that the entire Group has the same bone parent or remove all envelopes.",
},
'exporter_warn_source2names': {
	'en': "Consider renaming \"{0}\": in Source 2, model names can contain only lower-case characters, digits, and/or underscores.",
},
'exporter_warn_unicode': {
	'ja': "{0}「{1}」の名前はUnicode文字を含みます。間違ってコンパイルすることが可能です。",
	'en': "Name of {0} \"{1}\" contains Unicode characters. This may not compile correctly!",
},
'exporter_err_flexctrl_loadfail': {
	'en': "Could not load flex controllers. Python reports: {0}",
},
'qc_compile_err_nofiles': {
	'en': "Cannot compile, no QCs provided. The Blender Source Tools do not generate QCs.",
},
'exporter_err_missing_corrective_target': {
	'en': "Found corrective shape key \"{0}\", but not target shape \"{1}\"",
},
'qc_compile_complete': {
	'ja': "{0}つ「{1}」QCがコンパイルしました",
	'en': "Compiled {0} {1} QCs",
},
'exporter_err_shapes_decimate': {
	'en': "Cannot export shape keys from \"{0}\" because it has a '{1}' Decimate modifier. Only Un-Subdivide mode is supported.",
},
'exporterr_goldsrc_multiweights': {
	'en': "{0} verts on \"{1}\" have multiple weight links. GoldSrc does not support this!",
},
'exporter_err_splitvgroup_undefined': {
	'en': "Object \"{0}\" uses Vertex Group stereo split, but does not define a Vertex Group to use.",
},
'exporter_err_open': {
	'en': "Could not create {0} file. Python reports: {1}.",
},
'qc_compile_title': {
	'ja': "QCコンパイル",
	'en': "Compile QC",
},
'exporter_err_noexportables': {
	'en': "Found no valid objects for export",
},
'exporter_warn_sanitised_filename': {
	'en': "Sanitised exportable name \"{0}\" to \"{1}\"",
},
'exporter_warn_correctiveshape_duplicate': {
	'en': "Corrective shape key \"{0}\" has the same activation conditions ({1}) as \"{2}\". Skipping.",
},
'exporter_err_flexctrl_missing': {
	'en': "No flex controller defined for shape {0}.",
},
'qc_compile_err_compiler': {
	'en': "Could not execute studiomdl from \"{0}\"",
},
'exporter_err_facesnotex': {
	'en': "{0} faces on {1} did not have a Texture assigned",
},
'exporter_err_flexctrl_undefined': {
	'en': "Could not find flex controllers for \"{0}\"",
},
'exporter_warn_source2smdsupport': {
	'en': "Source 2 no longer supports SMD.",
},
'exporter_tip': {
	'en': "Export and compile Source Engine models",
},
'exporter_warn_weightlinks_culled': {
	'en': "{0} excess weight links beneath scene threshold of {1:0.2} culled on \"{2}\".",
},
'exporter_prop_scene_tip': {
	'en': "Export all items selected in the Source Engine Exportables panel",
},
'exporter_err_dmxenc': {
	'en': "DMX format \"Model {0}\" requires DMX encoding \"Binary 3\" or later",
},
'exporter_prop_group': {
	'ja': "グループの名前",
	'en': "Group Name",
},
'qc_compile_tip': {
	'en': "Compile QCs with the Source SDK",
},
'exporter_report_suffix': {
	'en': " with {0} Errors and {1} Warnings",
},
'exporter_err_groupempty': {
	'en': "Group {0} has no active objects",
},
'exporter_err_dmxother': {
	'en': "Cannot export DMX. Resolve errors with the SOURCE ENGINE EXPORT panel in SCENE PROPERTIES.",
},
'exporter_prop_group_tip': {
	'ja': "エクスポートにグループの名前",
	'en': "Name of the Group to export",
},
'exporter_warn_multiarmature': {
	'en': "Multiple armatures detected",
},
'exporter_err_solidifyinside': {
	'en': "Curve {0} has the Solidify modifier with rim fill, but is still exporting polys on both sides.",
},
'exporter_err_dupeenv_con': {
	'en': "Bone constraint \"{0}\" found on \"{1}\", which already has a bone parent. Ignoring.",
},
'exporter_err_unconfigured': {
	'en': "Scene unconfigured. See the SOURCE ENGINE EXPORT panel in SCENE PROPERTIES.",
},
'exporter_err_makedirs': {
	'en': "Could not create export folder. Python reports: {0}",
},
'exporter_warn_weightlinks_excess': {
	'en': "{0} verts on \"{1}\" have over {2} weight links. Source does not support this!",
},
'exporter_report_menu': {
	'ja': "レポート：Source Tools エラー",
	'en': "Source Tools Error Report",
},
'exporter_report': {
	'ja': "{0}つファイルは{1}秒エクスポート",
	'en': "{0} files exported in {1} seconds",
},
'exporter_err_groupmuted': {
	'ja': "ゲルーポ「{0}」はミュートです",
	'en': "Group {0} is suppressed",
},
'exporter_title': {
	'ja': "SMD/VTA/DMXをエクスポート",
	'en': "Export SMD/VTA/DMX",
},
'qc_compile_err_unknown': {
	'en': "Compile of {0} failed. Check the console for details",
},
'exporter_err_splitvgroup_missing': {
	'en': "Could not find stereo split Vertex Group \"{0}\" on object \"{1}\"",
},
'importer_complete': {
	'en': "Imported {0} files in {1} seconds",
},
'importer_bonemode': {
	'ja': "ボーンカスタムシェイプ",
	'en': "Bone shapes",
},
'importer_err_nofile': {
	'ja': "選択ファイルはありません",
	'en': "No file selected",
},
'importer_err_smd': {
	'en': "Could not open SMD file \"{0}\": {1}",
},
'importer_qc_macroskip': {
	'en': "Skipping macro in QC {0}",
},
'importer_bones_validate_desc': {
	'en': "Report new bones as missing without making any changes to the target Armature",
},
'importer_tip': {
	'en': "Imports uncompiled Source Engine model data",
},
'importer_title': {
	'ja': "インポート SMD/VTA, DMX, QC",
	'en': "Import SMD/VTA, DMX, QC",
},
'importer_makecamera': {
	'ja': "$originにカメラを生成",
	'en': "Make Camera At $origin",
},
'importer_bone_parent_miss': {
	'en': "Parent mismatch for bone \"{0}\": \"{1}\" in Blender, \"{2}\" in {3}.",
},
'importer_makecamera_tip': {
	'en': "For use in viewmodel editing; if not set, an Empty will be created instead",
},
'importer_err_shapetarget': {
	'en': "Could not import shape keys: no valid target object found",
},
'importer_rotmode_tip': {
	'en': "Determines the type of rotation Keyframes created when importing bones or animation",
},
'importer_skipremdoubles_tip': {
	'en': "Import raw, disconnected polygons from SMD files; these are harder to edit but a closer match to the original mesh",
},
'importer_balance_group': {
	'en': "DMX Stereo Balance",
},
'importer_bones_mode_desc': {
	'en': "How to behave when a reference mesh import introduces new bones to the target Armature (ignored for QCs)",
},
'importer_rotmode': {
	'ja': "回転モード",
	'en': "Rotation mode",
},
'importer_skipremdoubles': {
	'ja': "SMDのポリゴンと法線を保持",
	'en': "Preserve SMD Polygons & Normals",
},
'importer_bonemode_tip': {
	'en': "How bones in new Armatures should be displayed",
},
'importer_bones_append': {
	'ja': "対象で追加",
	'en': "Append to Target",
},
'importer_err_qci': {
	'en': "Could not open QC $include file \"{0}\" - skipping!",
},
'importer_up_tip': {
	'en': "Which axis represents 'up' (ignored for QCs)",
},
'importer_err_namelength': {
	'en': "{0} name \"{1}\" is too long to import. Truncating to \"{2}\"",
},
'importer_bones_append_desc': {
	'en': "Add new bones to the target Armature",
},
'importer_err_unmatched_mesh': {
	'en': "{0} VTA vertices ({1}%) were not matched to a mesh vertex! An object with a vertex group has been created to show where the VTA file's vertices are.",
},
'importer_bones_validate': {
	'ja': "対象で確認",
	'en': "Validate Against Target",
},
'importer_name_nomat': {
	'ja': "UndefinedMaterial",
	'en': "UndefinedMaterial",
},
'importer_bones_newarm_desc': {
	'en': "Make a new Armature for this import",
},
'importer_err_refanim': {
	'en': "Found animation in reference mesh \"{0}\", ignoring!",
},
'importer_bones_mode': {
	'ja': "ボーンの追加がモード",
	'en': "Bone Append Mode",
},
'importer_err_badweights': {
	'en': "{0} vertices weighted to invalid bones on {1}",
},
'importer_err_bonelimit_smd': {
	'en': "SMD only supports 128 bones!",
},
'importer_err_badfile': {
	'en': "Format of {0} not recognised",
},
'importer_err_smd_ver': {
	'en': "Unrecognised/invalid SMD file. Import will proceed, but may fail!",
},
'importer_doanims': {
	'ja': "アニメーションをインポート",
	'en': "Import Animations",
},
'importer_use_collections':{
	'en': "Create Collections",	
},
'importer_use_collections_tip':{
	'en': "Create a Blender collection for each imported mesh file. This retains the original file structure (important for DMX) and makes it easy to switch between LODs etc. with the number keys",
},
'importer_err_missingbones': {
	'en': "{0} contains {1} bones not present in {2}. Check the console for a list.",
},
'importer_err_noanimationbones': {
	'en': "No bones imported for animation {0}",
},
'importer_name_unmatchedvta': {
	'en': "Unmatched VTA",
},
'importer_bones_newarm': {
	'ja': "アーマティアを生成",
	'en': "Make New Armature",
},
'qc_warn_noarmature': {
	'en': "Skipping {0}; no armature found.",
},
'exportstate_pattern_tip': {
	'en': "Visible objects with this string in their name will be affected",
},
'exportstate': {
	'en': "Set Source Tools export state",
},
'activate_dep_shapes': {
	'en': "Activate Dependency Shapes",
},
'gen_block_success': {
	'en': "DMX written to text block \"{0}\"",
},
'gen_block': {
	'ja': "DMXフレックスのコントローラーの抜粋を生成します",
	'en': "Generate DMX Flex Controller block",
},
'vca_add_tip': {
	'en': "Add a Vertex Animation to the active Source Tools exportable",
},
'insert_uuid': {
	'en': "Insert UUID",
},
'launch_hlmv_tip': {
	'en': "Launches Half-Life Model Viewer",
},
'vertmap_remove': {
	'en': "Remove Source 2 Vertex Map",
},
'activate_dep_shapes_tip': {
	'en': "Activates shapes found in the name of the current shape (underscore delimited)",
},
'vca_qcgen_tip': {
	'en': "Copies a QC segment for this object's Vertex Animations to the clipboard",
},
'vca_remove_tip': {
	'en': "Remove the active Vertex Animation from the active Source Tools exportable",
},
'vca_add': {
	'en': "Add Vertex Animation",
},
'vertmap_select': {
	'en': "Select Source 2 Vertex Map",
},
'vca_preview': {
	'ja': "頂点アニメーションを再生します",
	'en': "Preview Vertex Animation",
},
'activate_dep_shapes_success': {
	'en': "Activated {0} dependency shapes",
},
'launch_hlmv': {
	'ja': "HLMVを開始",
	'en': "Launch HLMV",
},
'exportstate_pattern': {
	'en': "Search pattern",
},
'insert_uuid_tip': {
	'en': "Inserts a random UUID at the current location",
},
'gen_block_tip': {
	'en': "Generate a simple Flex Controller DMX block",
},
'gen_drivers': {
	'ja': "是正シェイプキーのドライバーを生成します",
	'en': "Generate Corrective Shape Key Drivers",
},
'apply_drivers':{
	'en': "Regenerate Shape Key Names From Drivers",
},
'apply_drivers_tip':{
	'en': "Renames corrective shape keys so that each their names are a combination of the shape keys that control them (via Blender animation drivers)",
},
'apply_drivers_success':{
	'en': "{0} shapes renamed.",
},
'vca_qcgen': {
	'ja': "QCの抜粋を生成します",
	'en': "Generate QC Segment",
},
'vertmap_create': {
	'en': "Create Source 2 Vertex Map",
},
'vca_preview_tip': {
	'en': "Plays the active Source Tools Vertex Animation using scene preview settings",
},
'vca_remove': {
	'en': "Remove Vertex Animation",
},
'gen_drivers_tip': {
	'en': "Adds Blender animation drivers to corrective Source engine shapes",
},
'qc_path': {
	'ja': "QCのパス",
	'en': "QC Path",
},
'engine_path': {
	'ja': "エンジンのパス",
	'en': "Engine Path",
},
'game_path_tip': {
	'en': "Directory containing gameinfo.txt (if unset, the system VPROJECT will be used)",
},
'visible_only': {
	'ja': "たった可視のレイヤー",
	'en': "Visible layers only",
},
'dmx_encoding': {
	'ja': "DMXの符号化",
	'en': "DMX encoding",
},
'game_path': {
	'ja': "ゲームのパス",
	'en': "Game Path",
},
'up_axis': {
	'ja': "対象の上昇軸",
	'en': "Target Up Axis",
},
'dmx_format': {
	'ja': "DMXのフォーマット",
	'en': "DMX format",
},
'ignore_materials': {
	'ja': "Blenderのマテリアルを軽視",
	'en': "Ignore Blender Materials",
},
'visible_only_tip': {
	'en': "Ignore objects in hidden layers",
},
'active_exportable': {
	'ja': "アクティブ・エクスポート可能",
	'en': "Active exportable",
},
'exportroot_tip': {
	'en': "The root folder into which SMD and DMX exports from this scene are written",
},
'qc_compilenow': {
	'ja': "今全てはコンパイル",
	'en': "Compile All Now",
},
'up_axis_tip': {
	'en': "Use for compatibility with data from other 3D tools",
},
'smd_format': {
	'ja': "対象のエンジン",
	'en': "Target Engine",
},
'dmx_mat_path_tip': {
	'en': "Folder relative to game root containing VMTs referenced in this scene (DMX only)",
},
'qc_compileall_tip': {
	'en': "Compile all QC files whenever anything is exported",
},
'qc_path_tip': {
	'en': "This scene's QC file(s); Unix wildcards supported",
},
'qc_nogamepath': {
	'en': "No Game Path and invalid VPROJECT",
},
'dmx_mat_path': {
	'ja': "マテリアルのパス",
	'en': "Material Path",
},
'exportroot': {
	'ja': "エクスポートのパス",
	'en': "Export Path",
},
'export_format': {
	'ja': "エクスポートのフォーマット",
	'en': "Export Format",
},
'qc_compileall': {
	'ja': "エクスポートから、みんあがコンパイル",
	'en': "Compile all on export",
},
'dmx_weightlinkcull': {
	'ja': "ウェイト・リンクの間引きのしきい値",
	'en': "Weight Link Cull Threshold",
},
'dmx_weightlinkcull_tip': {
	'en': "The maximum strength at which a weight link can be removed to comply with Source's per-vertex link limit",
},
'dmx_encoding_tip': {
	'en': "Manual override for binary DMX encoding version",
},
'dmx_format_tip': {
	'en': "Manual override for DMX model format version",
},
'engine_path_tip': {
	'en': "Directory containing studiomdl (Source 1) or resourcecompiler (Source 2)",
},
'ignore_materials_tip': {
	'en': "Only export face-assigned image filenames",
},
'updater_title': {
	'ja': "更新Source Toolsの確認",
	'en': "Check for Source Tools updates",
},
'update_err_downloadfailed': {
	'en': "Could not complete download:",
},
'offerchangelog_offer': {
	'en': "Restart Blender to complete the update. Click to view the changelog.",
},
'update_err_outdated': {
	'en': "The latest Source Tools require Blender {0}. Please upgrade.",
},
'update_err_unknown': {
	'en': "Could not install update:",
},
'offerchangelog_title': {
	'en': "Source Tools Update",
},
'update_err_corruption': {
	'en': "Update was downloaded, but file was not valid",
},
'update_done': {
	'en': "Installed Source Tools {0}!",
},
'updater_title_tip': {
	'en': "Connects to http://steamreview.org/BlenderSourceTools/latest.php",
},
'update_alreadylatest': {
	'en': "The latest Source Tools ({0}) are already installed.",
},
}

# === 简体中文翻译 (Simplified Chinese) ===
# 通过 get_id(id) 返回的英文原文，由 Blender 在界面语言设为“简体中文”时替换为下方译文。
_zh_CN = {
	'vca_sequence': '生成序列',
	'controllers_simple_tip': '为每个形态键生成一个 Flex 控制器',
	'vertmap_group_props': '顶点贴图',
	'action_selection_filter_tip': '所有匹配骨架筛选词且被使用的动作',
	'curve_poly_side_fwd': '前向（外侧）',
	'action_selection_current_tip': '骨架当前指定的动作或 NLA 轨道',
	'action_slot_selection_current_tip': '骨架当前激活的动作槽',
	'valvesource_cloth_enable': '启用布料物理',
	'subdir_tip': '相对于场景输出文件夹的可选路径',
	'controllers_mode': 'DMX Flex 控制器生成',
	'scene_export': '场景导出',
	'shape_stereo_mode_tip': '如何定义立体声拆分平衡',
	'bone_rot_legacy': '传统旋转',
	'controllers_advanced_tip': '插入现有 DMX 文件的 Flex 控制器',
	'triangulate_tip': '避免 Source 不支持的凹面 DMX 多边形',
	'action_filter': '动作筛选',
	'slot_filter': '动作槽筛选',
	'vca_start_tip': '开始记录顶点动画的场景帧',
	'action_filter_tip': '名称匹配此筛选模式且被使用的动作将被导出',
	'slot_filter_tip': '指定动作中名称匹配此通配符筛选模式的槽将被导出（留空则导出全部）',
	'shape_stereo_sharpness_tip': 'Flex 左右形态键从左侧到右侧的过渡锐度',
	'vca_sequence_tip': '导出时生成驱动此顶点动画的动画序列',
	'shape_stereo_mode': 'DMX 立体声拆分模式',
	'dummy_bone': '隐式静止骨骼',
	'vca_group_props': '顶点动画',
	'curve_poly_side': '多边形生成',
	'group_merge_mech': '合并机械部件',
	'action_selection_mode_tip': '如何为导出选择动作',
	'use_scene_export_tip': '随场景一起导出此项',
	'curve_poly_side_back': '后向（内侧）',
	'valvesource_vertex_blend': '混合参数 RGB',
	'bone_rot_legacy_tip': '将此骨架骨骼的 Y 轴重映射到 Z，以兼容旧版导入（仅 SMD）',
	'controller_source': 'DMX Flex 控制器来源',
	'group_suppress_tip': '分别导出此组的各个对象',
	'action_selection_current': '当前 / NLA',
	'action_slot_current': '当前动作槽',
	'shape_stereo_sharpness': 'DMX 立体声拆分锐度',
	'group_suppress': '抑制',
	'shape_stereo_vgroup': 'DMX 立体声拆分顶点组',
	'shape_stereo_vgroup_tip': '定义立体声平衡的顶点组（0=左，1=右）',
	'controllers_source_tip': '包含 Flex 控制器的 DMX 文件（或文本数据块）',
	'valvesource_vertex_blend1': '混合参数 附加 (?)',
	'curve_poly_side_tip': '决定导出时此曲线的哪一侧生成多边形',
	'triangulate': '三角化',
	'curve_poly_side_both': '两侧',
	'group_merge_mech_tip': '优化共享同一父级骨骼的网格的 DMX 导出',
	'action_selection_mode': '动作选择',
	'shape_stereo_mode_vgroup': '使用顶点组定义立体声平衡',
	'vca_end_tip': '停止记录顶点动画的场景帧',
	'valvesource_vertex_paint': '顶点绘制',
	'controllers_mode_tip': '如何定义 Flex 控制器',
	'subdir': '子文件夹',
	'dummy_bone_tip': '为不移动的顶点创建虚拟骨骼。模拟 Blender 在 Source 中的行为，但可能破坏与现有文件的兼容性（仅 SMD）',
	'exportpanel_steam': 'Steam 社区',
	'exportables_arm_filter_result': '"{0}" 个动作 ({1})',
	'exportables_arm_no_slot_filter': '"{1}" 的全部动作槽 ({0})',
	'exportables_flex_count_corrective': '矫正形态键：{0}',
	'exportables_curve_polyside': '多边形生成：',
	'exportmenu_title': 'Source 工具导出',
	'exportables_flex_help': 'Flex 控制器帮助',
	'exportpanel_title': 'Source 引擎导出',
	'exportables_flex_src': '控制器来源',
	'exportmenu_invalid': '无法导出所选对象',
	'qc_title': 'Source 引擎 QC 编译',
	'exportables_flex_props': 'Flex 属性',
	'exportables_flex_generate': '生成控制器',
	'exportables_flex_split': 'Flex 左右平衡：',
	'exportables_group_mute_suffix': '（已抑制）',
	'exportmenu_scene': '场景导出（{0} 个文件）',
	'exportpanel_dmxver': 'DMX 版本：',
	'exportpanel_update': '检查更新',
	'exportables_title': 'Source 引擎可导出项',
	'exportables_armature_props': '骨架属性 ({0})',
	'qc_bad_enginepath': '引擎路径无效',
	'qc_invalid_source2': 'Source 2 中不存在 QC 文件',
	'exportmenu_selected': '所选对象（{0} 个文件）',
	'exportables_group_props': '组属性',
	'qc_no_enginepath': '未提供引擎路径',
	'exportables_curve_props': '曲线属性',
	'exportables_flex_count': '形态键：{0}',
	'activate_dependency_shapes': '激活依赖形态键',
	'settings_prop': 'Blender Source 工具设置',
	'bl_info_description': 'Valve Software Source 引擎的导入与导出工具。支持 SMD\\VTA、DMX 与 QC。',
	'export_menuitem': 'Source 引擎（.smd、.vta、.dmx）',
	'help': '帮助',
	'bl_info_location': '文件 > 导入/导出，场景属性',
	'import_menuitem': 'Source 引擎（.smd、.vta、.dmx、.qc）',
	'exporter_err_nogroupitems': '组 "{0}" 中没有可导出的对象',
	'exporter_report_qc': '{0} 个文件已导出，{2} 个 QC 已编译（{3}/{4}），用时 {1} 秒',
	'exporter_err_relativeunsaved': '在保存 blend 文件之前无法导出到相对路径。',
	'exporter_err_nopolys': '对象 {0} 没有多边形，已跳过',
	'exporter_err_hidden': '跳过 {0}：对象无法被选中，可能是被动画驱动器隐藏。',
	'exporter_err_arm_nonuniform': '骨架 "{0}" 的缩放不均匀。Source 中的网格变形将与 Blender 不同。',
	'exporter_err_facesnotex_ormat': '{1} 上有 {0} 个面未指定材质或纹理',
	'exporter_err_arm_noanims': '找不到骨架 "{0}" 的任何动画',
	'exporter_err_dupeenv_arm': '在 "{1}" 上发现骨架修改器 "{0}"，该对象已有骨骼父级或约束。已忽略。',
	'exporter_err_bonelimit': '已导出 {0} 根骨骼，但 SMD 仅支持 {1} 根！',
	'exporter_err_unmergable': '跳过组 "{0}" 上的顶点动画，因其封套无法合并为单个 DMX 对象。修复方法：确保整个组使用相同的骨骼父级，或移除所有封套。',
	'exporter_warn_source2names': '建议重命名 "{0}"：在 Source 2 中，模型名称只能包含小写字母、数字和/或下划线。',
	'exporter_warn_unicode': '{0} "{1}" 的名称包含 Unicode 字符，可能无法正确编译！',
	'exporter_err_flexctrl_loadfail': '无法加载 Flex 控制器。Python 报告：{0}',
	'qc_compile_err_nofiles': '无法编译，未提供 QC 文件。Blender Source 工具不会生成 QC 文件。',
	'exporter_err_missing_corrective_target': '找到矫正形态键 "{0}"，但找不到目标形态键 "{1}"',
	'qc_compile_complete': '已编译 {0} 个 {1} QC',
	'exporter_err_shapes_decimate': '无法从 "{0}" 导出形态键，因为它带有 "{1}" 精简修改器。仅支持“取消细分”模式。',
	'exporterr_goldsrc_multiweights': '"{1}" 上有 {0} 个顶点具有多个权重链接。GoldSrc 不支持此情况！',
	'exporter_err_splitvgroup_undefined': '对象 "{0}" 使用了顶点组立体声拆分，但未指定要使用的顶点组。',
	'exporter_err_open': '无法创建 {0} 文件。Python 报告：{1}。',
	'qc_compile_title': '编译 QC',
	'exporter_err_noexportables': '未找到可供导出的有效对象',
	'exporter_warn_sanitised_filename': '已将可导出项名称 "{0}" 规范化为 "{1}"',
	'exporter_warn_correctiveshape_duplicate': '矫正形态键 "{0}" 与 "{2}" 的激活条件（{1}）相同。已跳过。',
	'exporter_err_flexctrl_missing': '形态键 {0} 未定义 Flex 控制器。',
	'qc_compile_err_compiler': '无法从 "{0}" 执行 studiomdl',
	'exporter_err_facesnotex': '{1} 上有 {0} 个面未指定纹理',
	'exporter_err_flexctrl_undefined': '找不到 "{0}" 的 Flex 控制器',
	'exporter_warn_source2smdsupport': 'Source 2 不再支持 SMD。',
	'exporter_tip': '导出并编译 Source 引擎模型',
	'exporter_warn_weightlinks_culled': '在 "{2}" 上剔除了 {0} 个低于场景阈值 {1:0.2} 的多余权重链接。',
	'exporter_prop_scene_tip': '导出 Source 引擎可导出项面板中选中的所有项',
	'exporter_err_dmxenc': 'DMX 格式 "Model {0}" 需要 DMX 编码 "Binary 3" 或更高版本',
	'exporter_prop_group': '组名称',
	'qc_compile_tip': '使用 Source SDK 编译 QC',
	'exporter_report_suffix': '，包含 {0} 个错误和 {1} 个警告',
	'exporter_err_groupempty': '组 {0} 没有激活的对象',
	'exporter_err_dmxother': '无法导出 DMX。请在“场景属性”的 SOURCE 引擎导出面板中解决错误。',
	'exporter_prop_group_tip': '要导出的组名称',
	'exporter_warn_multiarmature': '检测到多个骨架',
	'exporter_err_solidifyinside': '曲线 {0} 带有带边缘填充的实体化修改器，但仍导出了两侧多边形。',
	'exporter_err_dupeenv_con': '在 "{1}" 上发现骨骼约束 "{0}"，该对象已有骨骼父级。已忽略。',
	'exporter_err_unconfigured': '场景未配置。请参阅“场景属性”中的 SOURCE 引擎导出面板。',
	'exporter_err_makedirs': '无法创建导出文件夹。Python 报告：{0}',
	'exporter_warn_weightlinks_excess': '"{1}" 上有 {0} 个顶点拥有超过 {2} 个权重链接。Source 不支持此情况！',
	'exporter_report_menu': 'Source 工具错误报告',
	'exporter_report': '{0} 个文件已导出，用时 {1} 秒',
	'exporter_err_groupmuted': '组 {0} 已抑制',
	'exporter_title': '导出 SMD/VTA/DMX',
	'qc_compile_err_unknown': '{0} 的编译失败。请查看控制台获取详情',
	'exporter_err_splitvgroup_missing': '在对象 "{1}" 上找不到立体声拆分顶点组 "{0}"',
	'importer_complete': '已导入 {0} 个文件，用时 {1} 秒',
	'importer_bonemode': '骨骼形状',
	'importer_err_nofile': '未选择文件',
	'importer_err_smd': '无法打开 SMD 文件 "{0}"：{1}',
	'importer_qc_macroskip': '跳过 QC {0} 中的宏',
	'importer_bones_validate_desc': '将新骨骼报告为缺失，但不对目标骨架做任何更改',
	'importer_tip': '导入未编译的 Source 引擎模型数据',
	'importer_title': '导入 SMD/VTA、DMX、QC',
	'importer_makecamera': '在 $origin 处创建摄像机',
	'importer_bone_parent_miss': '骨骼 "{0}" 的父级不匹配：Blender 中为 "{1}"，{3} 中为 "{2}"。',
	'importer_makecamera_tip': '用于视图模型编辑；若未设置，将改为创建一个空对象',
	'importer_err_shapetarget': '无法导入形态键：未找到有效的目标对象',
	'importer_rotmode_tip': '决定导入骨骼或动画时创建的旋转关键帧类型',
	'importer_skipremdoubles_tip': '从 SMD 文件导入原始、断开的多边形；更难编辑，但更接近原始网格',
	'importer_balance_group': 'DMX 立体声平衡',
	'importer_bones_mode_desc': '当参考网格导入向目标骨架引入新骨骼时的行为（QC 忽略）',
	'importer_rotmode': '旋转模式',
	'importer_skipremdoubles': '保留 SMD 多边形与法线',
	'importer_bonemode_tip': '新骨架中的骨骼应如何显示',
	'importer_bones_append': '追加到目标',
	'importer_err_qci': '无法打开 QC $include 文件 "{0}" - 已跳过！',
	'importer_up_tip': '哪个轴代表“上”（QC 忽略）',
	'importer_err_namelength': '{0} 名称 "{1}" 过长，无法导入。将截断为 "{2}"',
	'importer_bones_append_desc': '向目标骨架添加新骨骼',
	'importer_err_unmatched_mesh': '{0} 个 VTA 顶点（{1}%）未匹配到网格顶点！已创建一个带顶点组的对象以显示 VTA 文件顶点的位置。',
	'importer_bones_validate': '与目标校验',
	'importer_name_nomat': 'UndefinedMaterial',
	'importer_bones_newarm_desc': '为此导入创建新骨架',
	'importer_err_refanim': '在参考网格 "{0}" 中发现动画，已忽略！',
	'importer_bones_mode': '骨骼追加模式',
	'importer_err_badweights': '{1} 上有 {0} 个顶点被赋予了无效的骨骼权重',
	'importer_err_bonelimit_smd': 'SMD 仅支持 128 根骨骼！',
	'importer_err_badfile': '无法识别 {0} 的格式',
	'importer_err_smd_ver': '无法识别/无效的 SMD 文件。导入将继续，但可能失败！',
	'importer_doanims': '导入动画',
	'importer_use_collections': '创建集合',
	'importer_use_collections_tip': '为每个导入的网格文件创建 Blender 集合。这会保留原始文件结构（对 DMX 很重要），并便于使用数字键在 LOD 之间切换',
	'importer_err_missingbones': '{0} 包含 {1} 根 {2} 中不存在的骨骼。请查看控制台获取列表。',
	'importer_err_noanimationbones': '未导入动画 {0} 的骨骼',
	'importer_name_unmatchedvta': '未匹配的 VTA',
	'importer_bones_newarm': '创建新骨架',
	'qc_warn_noarmature': '跳过 {0}；未找到骨架。',
	'exportstate_pattern_tip': '名称中包含此字符串的可见对象将受影响',
	'exportstate': '设置 Source 工具导出状态',
	'activate_dep_shapes': '激活依赖形态键',
	'gen_block_success': 'DMX 已写入文本块 "{0}"',
	'gen_block': '生成 DMX Flex 控制器块',
	'vca_add_tip': '向当前激活的 Source 工具可导出项添加顶点动画',
	'insert_uuid': '插入 UUID',
	'launch_hlmv_tip': '启动 Half-Life 模型查看器',
	'vertmap_remove': '移除 Source 2 顶点贴图',
	'activate_dep_shapes_tip': '激活当前形态键名称中包含的依赖形态键（以下划线分隔）',
	'vca_qcgen_tip': '将此对象的顶点动画的 QC 片段复制到剪贴板',
	'vca_remove_tip': '从当前激活的 Source 工具可导出项中移除活动顶点动画',
	'vca_add': '添加顶点动画',
	'vertmap_select': '选择 Source 2 顶点贴图',
	'vca_preview': '预览顶点动画',
	'activate_dep_shapes_success': '已激活 {0} 个依赖形态键',
	'launch_hlmv': '启动 HLMV',
	'exportstate_pattern': '搜索模式',
	'insert_uuid_tip': '在当前位置插入一个随机 UUID',
	'gen_block_tip': '生成一个简单的 Flex 控制器 DMX 块',
	'gen_drivers': '生成矫正形态键驱动器',
	'apply_drivers': '根据驱动器重新生成形态键名称',
	'apply_drivers_tip': '重命名矫正形态键，使其名称为控制它们的形态键的组合（通过 Blender 动画驱动器）',
	'apply_drivers_success': '{0} 个形态键已重命名。',
	'vca_qcgen': '生成 QC 片段',
	'vertmap_create': '创建 Source 2 顶点贴图',
	'vca_preview_tip': '使用场景预览设置播放当前激活的 Source 工具顶点动画',
	'vca_remove': '移除顶点动画',
	'gen_drivers_tip': '为 Source 引擎的矫正形态键添加 Blender 动画驱动器',
	'qc_path': 'QC 路径',
	'engine_path': '引擎路径',
	'game_path_tip': '包含 gameinfo.txt 的目录（若未设置，将使用系统 VPROJECT）',
	'visible_only': '仅可见层',
	'dmx_encoding': 'DMX 编码',
	'game_path': '游戏路径',
	'up_axis': '目标向上轴',
	'dmx_format': 'DMX 格式',
	'ignore_materials': '忽略 Blender 材质',
	'visible_only_tip': '忽略隐藏层中的对象',
	'active_exportable': '激活的可导出项',
	'exportroot_tip': '此场景的 SMD 和 DMX 导出写入的根文件夹',
	'qc_compilenow': '立即全部编译',
	'up_axis_tip': '用于与其他 3D 工具的数据兼容',
	'smd_format': '目标引擎',
	'dmx_mat_path_tip': '相对于游戏根目录、包含此场景引用的 VMT 的文件夹（仅 DMX）',
	'qc_compileall_tip': '每次导出任何内容时编译所有 QC 文件',
	'qc_path_tip': '此场景的 QC 文件；支持 Unix 通配符',
	'qc_nogamepath': '没有游戏路径且 VPROJECT 无效',
	'dmx_mat_path': '材质路径',
	'exportroot': '导出路径',
	'export_format': '导出格式',
	'qc_compileall': '导出时全部编译',
	'dmx_weightlinkcull': '权重链接剔除阈值',
	'dmx_weightlinkcull_tip': '为符合 Source 的每个顶点链接上限，权重链接可移除的最大强度',
	'dmx_encoding_tip': '手动覆盖二进制 DMX 编码版本',
	'dmx_format_tip': '手动覆盖 DMX 模型格式版本',
	'engine_path_tip': '包含 studiomdl（Source 1）或 resourcecompiler（Source 2）的目录',
	'ignore_materials_tip': '仅导出面分配的图像文件名',
	'updater_title': '检查 Source 工具更新',
	'update_err_downloadfailed': '无法完成下载：',
	'offerchangelog_offer': '重启 Blender 以完成更新。点击查看更新日志。',
	'update_err_outdated': '最新版 Source 工具需要 Blender {0}。请升级。',
	'update_err_unknown': '无法安装更新：',
	'offerchangelog_title': 'Source 工具更新',
	'update_err_corruption': '更新已下载，但文件无效',
	'update_done': '已安装 Source 工具 {0}！',
	'updater_title_tip': '连接到 http://steamreview.org/BlenderSourceTools/latest.php',
	'update_alreadylatest': '已安装最新版 Source 工具（{0}）。',
}

# 把散落在源码中的硬编码英文收编为翻译键（键 -> {英文, 中文}）
_data.update({
	'kv2_name': {'en': 'Write KeyValues2', 'zh_CN': '写入 KeyValues2'},
	'kv2_tip': {'en': 'Write ASCII DMX files', 'zh_CN': '写入 ASCII 格式的 DMX 文件'},
	'export_format_smd_desc': {'en': 'Studiomdl Data', 'zh_CN': 'Studiomdl 数据'},
	'export_format_dmx_desc': {'en': 'Datamodel Exchange', 'zh_CN': 'Datamodel 交换格式'},
	'smd_format_source_desc': {'en': 'Source Engine (Half-Life 2)', 'zh_CN': 'Source 引擎（半条命 2）'},
	'smd_format_goldsrc_desc': {'en': 'GoldSrc engine (Half-Life 1)', 'zh_CN': 'GoldSrc 引擎（半条命 1）'},
	'vertexanim_name': {'en': 'Name', 'zh_CN': '名称'},
	'vertexanim_start': {'en': 'Start', 'zh_CN': '起始帧'},
	'vertexanim_end': {'en': 'End', 'zh_CN': '结束帧'},
	'export_button': {'en': 'Export', 'zh_CN': '导出'},
	'qc_gen_report_copied': {'en': 'QC segment copied to clipboard.', 'zh_CN': 'QC 片段已复制到剪贴板。'},
	'button_add': {'en': 'Add', 'zh_CN': '添加'},
	'button_remove': {'en': 'Remove', 'zh_CN': '移除'},
	'flex_sharpness': {'en': 'Sharpness', 'zh_CN': '锐度'},
	'button_activate': {'en': 'Activate', 'zh_CN': '激活'},
	'exporter_filepath': {'en': 'File path', 'zh_CN': '文件路径'},
	'qc_compile_err_noselected': {'en': 'No QC files selected for compile.', 'zh_CN': '未选择要编译的 QC 文件。'},
	'importer_filepath': {'en': 'File Path', 'zh_CN': '文件路径'},
	'importer_filter_folders': {'en': 'Filter Folders', 'zh_CN': '过滤文件夹'},
	'importer_up_axis_name': {'en': 'Up Axis', 'zh_CN': '向上轴'},
	'importer_bonemode_default': {'en': 'Default', 'zh_CN': '默认'},
	'importer_bonemode_arrows': {'en': 'Arrows', 'zh_CN': '箭头'},
	'importer_bonemode_sphere': {'en': 'Sphere', 'zh_CN': '球体'},
})

# 将简体中文译文注入翻译表
for _k, _zh in _zh_CN.items():
	if _k in _data:
		_data[_k]['zh_CN'] = _zh
	else:
		_data[_k] = {'en': _k, 'zh_CN': _zh}

def _get_ids() -> dict[str,str]:	
	ids = {}
	for id,values in _data.items():
		ids[id] = values['en']
	return ids
ids = _get_ids()

# Blender 4.5+ 用 zh_HANS 表示简体中文，旧版本用 zh_CN；
# 两种代码都注册，保证在不同 Blender 版本下汉化都能生效。
_ZH_LOCALES = ('zh_CN', 'zh_HANS')

def _get_translations():
	import collections
	translations = collections.defaultdict(dict)
	for lang in _languages:
		out_langs = _ZH_LOCALES if lang == 'zh_CN' else (lang,)
		for out_lang in out_langs:
			for id,values in _data.items():
				value = values.get(lang)
				if value: translations[out_lang][(None, ids[id])] = value
	return translations
translations = _get_translations()
