# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_config_create.ui',
# licensing of 'model_config_create.ui' applies.
#
# Created: Mon Sep  2 14:10:18 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets


class Ui_model_config_create(object):
    def add_title(self, name, text, widget_num):

        label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        label.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        label.setObjectName(name + '_label')
        self.formLayout.setWidget(widget_num, QtWidgets.QFormLayout.LabelRole, label)

        label.setText(text)

        line = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        line.setObjectName(name + '_line')
        self.formLayout.setWidget(widget_num + 1, QtWidgets.QFormLayout.SpanningRole, line)

        return widget_num + 2

    def add_lineedit(self, name, widget_num):
        lineedit = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        lineedit.setObjectName(name + '_lineedit')
        self.formLayout.setWidget(widget_num, QtWidgets.QFormLayout.FieldRole, lineedit)

    def add_checkbox(self, name, widget_num):
        checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        checkbox.setText("")
        checkbox.setChecked(True)
        checkbox.setObjectName(name + '_checkbox')
        self.formLayout.setWidget(widget_num, QtWidgets.QFormLayout.FieldRole, checkbox)

    def add_combobox(self, name, widget_num, options):
        combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        combobox.setObjectName(name + '_combobox')
        combobox.addItem("")
        for option in options:
            combobox.addItem(option)
        self.formLayout.setWidget(widget_num, QtWidgets.QFormLayout.FieldRole, combobox)

    def add_form_pair(self, name, widget_num, widget_type='Numeric', text=None, options=None):

        label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        label.setObjectName(name + '_label')
        self.formLayout.setWidget(widget_num, QtWidgets.QFormLayout.LabelRole, label)
        if not text:
            text = name

        label.setText(text)

        if widget_type == 'Numeric':
            self.add_lineedit(name, widget_num)
        elif widget_type == 'Check':
            self.add_checkbox(name, widget_num)
        elif widget_type == 'Combo':
            self.add_combobox(name, widget_num, options)

        return widget_num + 1

    def setupUi(self, model_config_create):
        model_config_create.setObjectName("model_config_create")
        model_config_create.resize(600, 440)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(model_config_create.sizePolicy().hasHeightForWidth())
        model_config_create.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(model_config_create)
        self.centralwidget.setObjectName("centralwidget")
        self.centralLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.centralLayout.setSpacing(0)
        self.centralLayout.setContentsMargins(0, 0, 0, 0)
        self.centralLayout.setObjectName("centralLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, -785, 584, 1179))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        widget_num = self.add_title('model', "Model Parameters (func)", 0)
        # self.label_62 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_62.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        # self.label_62.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        # self.label_62.setObjectName("model_title")
        # self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_62)
        # self.line_7 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_7.setObjectName("line_7")
        # self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.line_7)

        self.add_form_pair('model_name', widget_num)
        # self.label_52 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_52.setObjectName("label_52")
        # self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_52)
        # self.model_name_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        # self.model_name_text.setObjectName("model_name_text")
        # self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.model_name_text)

        self.label_47 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_47.setObjectName("label_47")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_47)
        self.output_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.output_text.setObjectName("output_text")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.output_text)
        self.label_42 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_42.setObjectName("label_42")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_42)
        self.num_classes_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.num_classes_text.setObjectName("num_classes_text")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.num_classes_text)
        self.label_34 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_34.setObjectName("label_34")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_34)
        self.num_channels_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.num_channels_text.setObjectName("num_channels_text")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.num_channels_text)
        self.label_56 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_56.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        self.label_56.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_56.setObjectName("label_56")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_56)
        self.line_10 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.SpanningRole, self.line_10)
        self.label_64 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_64.setObjectName("label_64")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_64)
        self.normal_fms_num_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.normal_fms_num_text.setObjectName("normal_fms_num_text")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.normal_fms_num_text)
        self.label_44 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_44.setObjectName("label_44")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_44)
        self.normal_kernel_dims_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.normal_kernel_dims_text.setObjectName("normal_kernel_dims_text")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.normal_kernel_dims_text)
        self.label_41 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_41.setObjectName("label_41")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.label_41)
        self.normal_res_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.normal_res_text.setObjectName("normal_res_text")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.normal_res_text)
        self.label_49 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_49.setObjectName("label_49")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.LabelRole, self.label_49)
        self.normal_lower_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.normal_lower_text.setObjectName("normal_lower_text")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.normal_lower_text)
        self.label_46 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_46.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        self.label_46.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_46)
        self.line_9 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.SpanningRole, self.line_9)
        self.sub_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)

        self.add_form_pair('sub', 14, widget_type='Check')
        # self.sub_label.setObjectName("sub_label")
        # self.formLayout.setWidget(14, QtWidgets.QFormLayout.LabelRole, self.sub_label)
        # self.sub_checkbox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        # self.sub_checkbox.setText("")
        # self.sub_checkbox.setChecked(True)
        # self.sub_checkbox.setObjectName("sub_checkbox")
        # self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.sub_checkbox)

        self.sub_fms_num_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sub_fms_num_label.setObjectName("sub_fms_num_label")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.LabelRole, self.sub_fms_num_label)
        self.sub_fms_num_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sub_fms_num_text.setObjectName("sub_fms_num_text")
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.sub_fms_num_text)
        self.sub_kernel_dims_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sub_kernel_dims_label.setObjectName("sub_kernel_dims_label")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.LabelRole, self.sub_kernel_dims_label)
        self.sub_kernel_dims_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sub_kernel_dims_text.setObjectName("sub_kernel_dims_text")
        self.formLayout.setWidget(16, QtWidgets.QFormLayout.FieldRole, self.sub_kernel_dims_text)
        self.sub_factor_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sub_factor_label.setObjectName("sub_factor_label")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.LabelRole, self.sub_factor_label)
        self.sub_factor_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sub_factor_text.setObjectName("sub_factor_text")
        self.formLayout.setWidget(17, QtWidgets.QFormLayout.FieldRole, self.sub_factor_text)
        self.sub_res_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sub_res_label.setObjectName("sub_res_label")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.LabelRole, self.sub_res_label)
        self.sub_res_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sub_res_text.setObjectName("sub_res_text")
        self.formLayout.setWidget(18, QtWidgets.QFormLayout.FieldRole, self.sub_res_text)
        self.sub_lower_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.sub_lower_label.setObjectName("sub_lower_label")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.LabelRole, self.sub_lower_label)
        self.sub_lower_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.sub_lower_text.setObjectName("sub_lower_text")
        self.formLayout.setWidget(19, QtWidgets.QFormLayout.FieldRole, self.sub_lower_text)

        self.add_title('fc', "Fully Connected Layers (func)", 20)

        # self.label_53 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_53.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        # self.label_53.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        # self.label_53.setObjectName("label_53")
        # self.formLayout.setWidget(20, QtWidgets.QFormLayout.LabelRole, self.label_53)
        # self.line_12 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        # self.line_12.setFrameShape(QtWidgets.QFrame.HLine)
        # self.line_12.setFrameShadow(QtWidgets.QFrame.Sunken)
        # self.line_12.setObjectName("line_12")
        # self.formLayout.setWidget(21, QtWidgets.QFormLayout.SpanningRole, self.line_12)

        self.label_38 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_38.setObjectName("label_38")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.LabelRole, self.label_38)
        self.fc_fms_num_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fc_fms_num_text.setObjectName("fc_fms_num_text")
        self.formLayout.setWidget(22, QtWidgets.QFormLayout.FieldRole, self.fc_fms_num_text)
        self.label_61 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_61.setObjectName("label_61")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.LabelRole, self.label_61)
        self.fc_kernel_dims_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fc_kernel_dims_text.setObjectName("fc_kernel_dims_text")
        self.formLayout.setWidget(23, QtWidgets.QFormLayout.FieldRole, self.fc_kernel_dims_text)
        self.label_59 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_59.setObjectName("label_59")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.LabelRole, self.label_59)
        self.fc_res_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.fc_res_text.setObjectName("fc_res_text")
        self.formLayout.setWidget(24, QtWidgets.QFormLayout.FieldRole, self.fc_res_text)
        self.label_35 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_35.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        self.label_35.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_35.setObjectName("label_35")
        self.formLayout.setWidget(25, QtWidgets.QFormLayout.LabelRole, self.label_35)
        self.line_8 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.formLayout.setWidget(26, QtWidgets.QFormLayout.SpanningRole, self.line_8)
        self.label_57 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_57.setObjectName("label_57")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.LabelRole, self.label_57)
        self.seg_train_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.seg_train_text.setObjectName("seg_train_text")
        self.formLayout.setWidget(27, QtWidgets.QFormLayout.FieldRole, self.seg_train_text)
        self.label_40 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_40.setObjectName("label_40")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.LabelRole, self.label_40)
        self.seg_val_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.seg_val_text.setObjectName("seg_val_text")
        self.formLayout.setWidget(28, QtWidgets.QFormLayout.FieldRole, self.seg_val_text)
        self.label_60 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_60.setObjectName("label_60")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.LabelRole, self.label_60)
        self.seg_inf_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.seg_inf_text.setObjectName("seg_inf_text")
        self.formLayout.setWidget(29, QtWidgets.QFormLayout.FieldRole, self.seg_inf_text)
        self.label_55 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_55.setStyleSheet("font: 75 15pt \"Ubuntu Condensed\";")
        self.label_55.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_55.setObjectName("label_55")
        self.formLayout.setWidget(30, QtWidgets.QFormLayout.LabelRole, self.label_55)
        self.line_11 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.line_11.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_11.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_11.setObjectName("line_11")
        self.formLayout.setWidget(31, QtWidgets.QFormLayout.SpanningRole, self.line_11)
        self.label_50 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_50.setObjectName("label_50")
        self.formLayout.setWidget(32, QtWidgets.QFormLayout.LabelRole, self.label_50)
        self.drop_normal_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.drop_normal_text.setObjectName("drop_normal_text")
        self.formLayout.setWidget(32, QtWidgets.QFormLayout.FieldRole, self.drop_normal_text)
        self.label_66 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_66.setObjectName("label_66")
        self.formLayout.setWidget(33, QtWidgets.QFormLayout.LabelRole, self.label_66)
        self.drop_sub_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.drop_sub_text.setObjectName("drop_sub_text")
        self.formLayout.setWidget(33, QtWidgets.QFormLayout.FieldRole, self.drop_sub_text)
        self.label_43 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_43.setObjectName("label_43")
        self.formLayout.setWidget(34, QtWidgets.QFormLayout.LabelRole, self.label_43)
        self.drop_fc_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.drop_fc_text.setObjectName("drop_fc_text")
        self.formLayout.setWidget(34, QtWidgets.QFormLayout.FieldRole, self.drop_fc_text)

        self.add_form_pair('kernel_init', 35, widget_type='Combo', options=['fanIn', 'normal'])
        # self.label_51 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        # self.label_51.setObjectName("label_51")
        # self.formLayout.setWidget(35, QtWidgets.QFormLayout.LabelRole, self.label_51)
        #
        # self.kernel_init_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        # self.kernel_init_combobox.setObjectName("kernel_init_combobox")
        # self.kernel_init_combobox.addItem("")
        # self.kernel_init_combobox.setItemText(0, "")
        # self.kernel_init_combobox.addItem("")
        # self.kernel_init_combobox.addItem("")
        # self.formLayout.setWidget(35, QtWidgets.QFormLayout.FieldRole, self.kernel_init_combobox)

        self.init_scale_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.init_scale_label.setObjectName("init_scale_label")
        self.formLayout.setWidget(37, QtWidgets.QFormLayout.LabelRole, self.init_scale_label)
        self.init_scale_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.init_scale_text.setObjectName("init_scale_text")
        self.formLayout.setWidget(37, QtWidgets.QFormLayout.FieldRole, self.init_scale_text)
        self.label_39 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_39.setObjectName("label_39")
        self.formLayout.setWidget(38, QtWidgets.QFormLayout.LabelRole, self.label_39)
        self.activation_combobox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.activation_combobox.setObjectName("activation_combobox")
        self.activation_combobox.addItem("")
        self.activation_combobox.setItemText(3, "")
        self.activation_combobox.addItem("")
        self.activation_combobox.addItem("")
        self.activation_combobox.addItem("")
        self.activation_combobox.addItem("")
        self.activation_combobox.addItem("")
        self.formLayout.setWidget(38, QtWidgets.QFormLayout.FieldRole, self.activation_combobox)
        self.label_58 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_58.setObjectName("label_58")
        self.formLayout.setWidget(39, QtWidgets.QFormLayout.LabelRole, self.label_58)
        self.bn_batch_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.bn_batch_text.setObjectName("bn_batch_text")
        self.formLayout.setWidget(39, QtWidgets.QFormLayout.FieldRole, self.bn_batch_text)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(40, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.save_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.save_button.setObjectName("save_button")
        self.formLayout.setWidget(41, QtWidgets.QFormLayout.SpanningRole, self.save_button)
        self.init_std_label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.init_std_label.setObjectName("init_std_label")
        self.formLayout.setWidget(36, QtWidgets.QFormLayout.LabelRole, self.init_std_label)
        self.init_std_text = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.init_std_text.setObjectName("init_std_text")
        self.formLayout.setWidget(36, QtWidgets.QFormLayout.FieldRole, self.init_std_text)
        self.horizontalLayout.addLayout(self.formLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.centralLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        model_config_create.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(model_config_create)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        model_config_create.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(model_config_create)
        self.statusbar.setObjectName("statusbar")
        model_config_create.setStatusBar(self.statusbar)
        self.action_open = QtWidgets.QAction(model_config_create)
        self.action_open.setObjectName("action_open")
        self.action_save_as = QtWidgets.QAction(model_config_create)
        self.action_save_as.setObjectName("action_save_as")
        self.action_clear_all = QtWidgets.QAction(model_config_create)
        self.action_clear_all.setObjectName("action_clear_all")
        self.action_close = QtWidgets.QAction(model_config_create)
        self.action_close.setObjectName("action_close")
        self.action_save = QtWidgets.QAction(model_config_create)
        self.action_save.setObjectName("action_save")
        self.action_load = QtWidgets.QAction(model_config_create)
        self.action_load.setObjectName("action_load")
        self.menuFile.addAction(self.action_open)
        self.menuFile.addAction(self.action_load)
        self.menuFile.addAction(self.action_save)
        self.menuFile.addAction(self.action_save_as)
        self.menuFile.addAction(self.action_close)
        self.menuEdit.addAction(self.action_clear_all)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())

        self.retranslateUi(model_config_create)
        # self.kernel_init_combobox.setCurrentIndex(1)
        # self.activation_combobox.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(model_config_create)

    def retranslateUi(self, model_config_create):
        model_config_create.setWindowTitle(QtWidgets.QApplication.translate("model_config_create", "Create Model Config", None, -1))
        # self.label_62.setText(QtWidgets.QApplication.translate("model_config_create", "Model Parameters", None, -1))
        # self.label_52.setText(QtWidgets.QApplication.translate("model_config_create", "Model Name", None, -1))
        # self.model_name_text.setText(QtWidgets.QApplication.translate("model_config_create", "deepMedic", None, -1))
        self.label_47.setText(QtWidgets.QApplication.translate("model_config_create", "Output Folder", None, -1))
        self.output_text.setText(QtWidgets.QApplication.translate("model_config_create", "../../../output", None, -1))
        self.label_42.setText(QtWidgets.QApplication.translate("model_config_create", "Number of Classes", None, -1))
        self.num_classes_text.setText(QtWidgets.QApplication.translate("model_config_create", "5", None, -1))
        self.label_34.setText(QtWidgets.QApplication.translate("model_config_create", "Number of Channels", None, -1))
        self.num_channels_text.setText(QtWidgets.QApplication.translate("model_config_create", "2", None, -1))
        self.label_56.setText(QtWidgets.QApplication.translate("model_config_create", "Normal Pathway", None, -1))
        self.label_64.setText(QtWidgets.QApplication.translate("model_config_create", "Number of Feature Maps per Layer", None, -1))
        self.normal_fms_num_text.setText(QtWidgets.QApplication.translate("model_config_create", "[30, 30, 40, 40, 40, 40, 50, 50]", None, -1))
        self.label_44.setText(QtWidgets.QApplication.translate("model_config_create", "Kernel Dimensions per Layer", None, -1))
        self.normal_kernel_dims_text.setText(QtWidgets.QApplication.translate("model_config_create", "[[3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3]]", None, -1))
        self.label_41.setText(QtWidgets.QApplication.translate("model_config_create", "Layers with Residual Connections", None, -1))
        self.normal_res_text.setText(QtWidgets.QApplication.translate("model_config_create", "[4,6,8]", None, -1))
        self.label_49.setText(QtWidgets.QApplication.translate("model_config_create", "Lower Rank Layers", None, -1))
        self.normal_lower_text.setText(QtWidgets.QApplication.translate("model_config_create", "[]", None, -1))
        self.label_46.setText(QtWidgets.QApplication.translate("model_config_create", "Subsampled Pathway", None, -1))
        # self.sub_label.setText(QtWidgets.QApplication.translate("model_config_create", "Use Subampled Pathway", None, -1))
        self.sub_fms_num_label.setText(QtWidgets.QApplication.translate("model_config_create", "Number of Feature Maps per Layer", None, -1))
        self.sub_fms_num_text.setText(QtWidgets.QApplication.translate("model_config_create", "[30, 30, 40, 40, 40, 40, 50, 50]", None, -1))
        self.sub_kernel_dims_label.setText(QtWidgets.QApplication.translate("model_config_create", "Kernel Dimensions per Layer", None, -1))
        self.sub_kernel_dims_text.setText(QtWidgets.QApplication.translate("model_config_create", "[[3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3], [3,3,3]]", None, -1))
        self.sub_factor_label.setText(QtWidgets.QApplication.translate("model_config_create", "Subsample Factor", None, -1))
        self.sub_factor_text.setText(QtWidgets.QApplication.translate("model_config_create", "[[3,3,3],[5,5,5]]", None, -1))
        self.sub_res_label.setText(QtWidgets.QApplication.translate("model_config_create", "Layers with Residual Connections", None, -1))
        self.sub_res_text.setText(QtWidgets.QApplication.translate("model_config_create", "[4,6,8]", None, -1))
        self.sub_lower_label.setText(QtWidgets.QApplication.translate("model_config_create", "Lower Rank Layers", None, -1))
        self.sub_lower_text.setText(QtWidgets.QApplication.translate("model_config_create", "[]", None, -1))
        # self.label_53.setText(QtWidgets.QApplication.translate("model_config_create", "Fully Connected Layers", None, -1))
        self.label_38.setText(QtWidgets.QApplication.translate("model_config_create", "Number of Feature Maps per Layer", None, -1))
        self.fc_fms_num_text.setText(QtWidgets.QApplication.translate("model_config_create", "[250, 250]", None, -1))
        self.label_61.setText(QtWidgets.QApplication.translate("model_config_create", "Kernel Dimensions for 1st Layer", None, -1))
        self.fc_kernel_dims_text.setText(QtWidgets.QApplication.translate("model_config_create", "[3,3,3]", None, -1))
        self.label_59.setText(QtWidgets.QApplication.translate("model_config_create", "Layers with Residual Connections", None, -1))
        self.fc_res_text.setText(QtWidgets.QApplication.translate("model_config_create", "[2]", None, -1))
        self.label_35.setText(QtWidgets.QApplication.translate("model_config_create", "Size of Image Segments", None, -1))
        self.label_57.setText(QtWidgets.QApplication.translate("model_config_create", "Size of Training Segments", None, -1))
        self.seg_train_text.setText(QtWidgets.QApplication.translate("model_config_create", "[37,37,37]", None, -1))
        self.label_40.setText(QtWidgets.QApplication.translate("model_config_create", "Size of Validation Segments", None, -1))
        self.seg_val_text.setText(QtWidgets.QApplication.translate("model_config_create", "[17,17,17]", None, -1))
        self.label_60.setText(QtWidgets.QApplication.translate("model_config_create", "Size of Inference Segments", None, -1))
        self.seg_inf_text.setText(QtWidgets.QApplication.translate("model_config_create", "[45,45,45]", None, -1))
        self.label_55.setText(QtWidgets.QApplication.translate("model_config_create", "Other Options", None, -1))
        self.label_50.setText(QtWidgets.QApplication.translate("model_config_create", "Dropout Rates Normal Pathway", None, -1))
        self.drop_normal_text.setText(QtWidgets.QApplication.translate("model_config_create", "[]", None, -1))
        self.label_66.setText(QtWidgets.QApplication.translate("model_config_create", "Dropout Rates Subsampled Pathway", None, -1))
        self.drop_sub_text.setText(QtWidgets.QApplication.translate("model_config_create", "[]", None, -1))
        self.label_43.setText(QtWidgets.QApplication.translate("model_config_create", "Dropout Rates FC layers", None, -1))
        self.drop_fc_text.setText(QtWidgets.QApplication.translate("model_config_create", "[0.0, 0.5, 0.5] ", None, -1))
        # self.label_51.setText(QtWidgets.QApplication.translate("model_config_create", "Initialisation Method for Kernel Weights", None, -1))
        # self.kernel_init_combobox.setItemText(1, QtWidgets.QApplication.translate("model_config_create", "fanIn", None, -1))
        # self.kernel_init_combobox.setItemText(2, QtWidgets.QApplication.translate("model_config_create", "normal", None, -1))
        self.init_scale_label.setText(QtWidgets.QApplication.translate("model_config_create", "Initialisation Scale", None, -1))
        self.init_scale_text.setText(QtWidgets.QApplication.translate("model_config_create", "2", None, -1))
        self.label_39.setText(QtWidgets.QApplication.translate("model_config_create", "Activation Function", None, -1))
        self.activation_combobox.setItemText(4, QtWidgets.QApplication.translate("model_config_create", "prelu", None, -1))
        self.activation_combobox.setItemText(5, QtWidgets.QApplication.translate("model_config_create", "linear", None, -1))
        self.activation_combobox.setItemText(6, QtWidgets.QApplication.translate("model_config_create", "relu", None, -1))
        self.activation_combobox.setItemText(7, QtWidgets.QApplication.translate("model_config_create", "elu", None, -1))
        self.activation_combobox.setItemText(8, QtWidgets.QApplication.translate("model_config_create", "selu", None, -1))
        self.label_58.setText(QtWidgets.QApplication.translate("model_config_create", "Number of Batches for Batch Norm Rolling Average ", None, -1))
        self.bn_batch_text.setText(QtWidgets.QApplication.translate("model_config_create", "60", None, -1))
        self.save_button.setText(QtWidgets.QApplication.translate("model_config_create", "Save Configuration File", None, -1))
        self.init_std_label.setText(QtWidgets.QApplication.translate("model_config_create", "Initialisation Standard Deviation", None, -1))
        self.menuFile.setTitle(QtWidgets.QApplication.translate("model_config_create", "&File", None, -1))
        self.menuEdit.setTitle(QtWidgets.QApplication.translate("model_config_create", "&Edit", None, -1))
        self.action_open.setText(QtWidgets.QApplication.translate("model_config_create", "&Open...", None, -1))
        self.action_open.setToolTip(QtWidgets.QApplication.translate("model_config_create", "Open", None, -1))
        self.action_open.setShortcut(QtWidgets.QApplication.translate("model_config_create", "Ctrl+O", None, -1))
        self.action_save_as.setText(QtWidgets.QApplication.translate("model_config_create", "Save &As...", None, -1))
        self.action_save_as.setShortcut(QtWidgets.QApplication.translate("model_config_create", "Ctrl+Shift+S", None, -1))
        self.action_clear_all.setText(QtWidgets.QApplication.translate("model_config_create", "&Clear All Fields", None, -1))
        self.action_clear_all.setShortcut(QtWidgets.QApplication.translate("model_config_create", "Ctrl+N", None, -1))
        self.action_close.setText(QtWidgets.QApplication.translate("model_config_create", "&Close Window", None, -1))
        self.action_save.setText(QtWidgets.QApplication.translate("model_config_create", "&Save", None, -1))
        self.action_save.setShortcut(QtWidgets.QApplication.translate("model_config_create", "Ctrl+S", None, -1))
        self.action_load.setText(QtWidgets.QApplication.translate("model_config_create", "&Load...", None, -1))

