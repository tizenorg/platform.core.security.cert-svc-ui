/*
 * Copyright (c) 2011 Samsung Electronics Co., Ltd All Rights Reserved
 *
 *    Licensed under the Apache License, Version 2.0 (the "License");
 *    you may not use this file except in compliance with the License.
 *    You may obtain a copy of the License at
 *
 *        http://www.apache.org/licenses/LICENSE-2.0
 *
 *    Unless required by applicable law or agreed to in writing, software
 *    distributed under the License is distributed on an "AS IS" BASIS,
 *    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *    See the License for the specific language governing permissions and
 *    limitations under the License.
 */
/*
 * @file        cert-selection-uigadget.h
 * @author      Janusz Kozerski (j.kozerski@samsung.com)
 * @version     1.0
 */

#ifndef __UG_SETTING_MANAGE_APPLICATION_EFL_H__
#define __UG_SETTING_MANAGE_APPLICATION_EFL_H__

#include <Elementary.h>
#include <ui-gadget.h>
#include <ui-gadget-module.h>
#include <glib.h>
#include <app.h>

#ifndef PACKAGE
#define PACKAGE "ug-setting-manage-certificates-efl"
#endif

#ifndef LOCALEDIR
#define LOCALEDIR PREFIX"/res/locale"
#endif

#define IMAGE_PATH PREFIX"/res/images"

struct ug_data {
    Evas_Object         *win_main;
    Evas_Object         *bg;
    Evas_Object         *layout_main;
    Evas_Object         *navi_bar;
    GList               *view_list;
    ui_gadget_h         ug;
    ui_gadget_h         sub_ug;
    service_h           *service;
    void                *data;

    //Evas_Object         *popup;
    //Evas_Object *indicator;
    //Ecore_Pipe *msg_pipe;

};

struct ug_data *get_ug_data();

void cert_selection_cb(void *data, Evas_Object *obj, void *event_info);

#endif /* __UG_SETTING_MANAGE_APPLICATION_EFL_H__ */
