from utils.torch_utils import device_list, default_device, str_to_dtype
from utils.hf_utils import list_local_models
import torch

node_devices = device_list.copy()
node_devices['auto'] = { "index": 0, "device": "cpu", "host": '', "label": "auto", "total_memory": None }
del node_devices['cpu']

MODULE_MAP = {
    'DiffusionPipelineLoader': {
        'label': 'Diffusion Pipeline Loader',
        'style': {
            'minWidth': '320px',
        },
        'params': {
            'diffusion_pipeline': {
                'label': 'Pipeline',
                'display': 'output',
                'type': 'DiffusionPipeline',
            },
            'model_id': {
                'label': 'Model ID',
                'type': 'string',
                'options': list_local_models(),
                'display': 'autocomplete',
                'no_validation': True,
                'default': '',
            },
            'online_status': {
                'label': 'Online Status',
                'type': 'string',
                'options': [ 'Always online', 'Connect if needed', 'Local files only' ],
                'default': 'Connect if needed',
            },
            'dtype': {
                'label': 'Dtype',
                'type': 'string',
                'options': [ 'auto', 'float32', 'float16', 'bfloat16', 'float8_e4m3fn' ],
                'default': 'bfloat16',
                'postProcess': str_to_dtype,
            },
            'load_strategy': {
                'label': 'CPU Offload',
                'type': 'string',
                'options': [ 'None', 'Model cpu offload', 'Sequential cpu offload' ],
                'default': 'None',
            },
            'variant': {
                'label': 'Variant',
                'type': 'string',
                #'options': [ 'fp16', 'ema' ],
                #'display': 'autocomplete',
                'default': '',
                'group': { 'key': 'more_options', 'label': 'More Options', 'display': 'collapse' },
            },
            'revision': {
                'label': 'Revision',
                'type': 'string',
                'default': '',
                'group': 'more_options',
            },
            'device': {
                'label': 'Device',
                'type': 'string',
                'options': node_devices,
                'default': 'auto',
                'group': 'more_options',
            },
            'use_safetensors': {
                'label': 'Use safetensors',
                'type': 'boolean',
                'default': False,
                'group': 'more_options',
            },
        },
    },

    'DiffusionPipelineSampler': {
        'label': 'Diffusion Pipeline Sampler',
        'params': {
            'diffusion_pipeline': {
                'label': 'Pipeline',
                'type': 'DiffusionPipeline',
                'display': 'input',
            },
            'seed': {
                'label': 'Seed',
                'type': 'int',
                'display': 'number',
                'default': 42,
                'min': 0,
                #'max': 2**32 - 1,
            },
            'width': {
                'label': 'Width',
                'type': 'int',
                'display': 'text',
                'default': 1024,
                'min': 8,
                'max': 8192,
                'step': 8,
                'group': 'dimensions',
            },
            'height': {
                'label': 'Height',
                'type': 'int',
                'display': 'text',
                'default': 1024,
                'min': 8,
                'max': 8192,
                'step': 8,
                'group': 'dimensions',
            },
            'resolution_picker': {
                'label': 'Resolution',
                'display': 'ui',
                'type': 'dropdownIcon',
                'options': [
                    { 'label': ' 720×1280 (9:16)', 'value': [720, 1280] },
                    { 'label': ' 768×1344 (0.57)', 'value': [768, 1344] },
                    { 'label': ' 768×1280 (3:5)', 'value': [768, 1280] },
                    { 'label': ' 832×1152 (3:4)', 'value': [832, 1152] },
                    { 'label': '1024×1024 (1:1)', 'value': [1024, 1024] },
                    { 'label': '  768×768 (1:1)', 'value': [768, 768] },
                    { 'label': '  512×512 (1:1)', 'value': [512, 512] },
                    { 'label': ' 1152×832 (4:3)', 'value': [1152, 832] },
                    { 'label': ' 1280×768 (5:3)', 'value': [1280, 768] },
                    { 'label': ' 1344×768 (1.75)', 'value': [1344, 768] },
                    { 'label': ' 1280×720 (16:9)', 'value': [1280, 720] },
                ],
                'target': ['width', 'height'],
                'group': 'dimensions',
            },
            'prompt': {
                'label': 'Prompt',
                'type': 'string',
                'display': 'textarea',
            },
            'steps': {
                'label': 'Steps',
                'type': 'int',
                'default': 25,
                'min': 1,
                'max': 1000,
            },
            'cfg': {
                'label': 'CFG',
                'type': 'float',
                'default': 7.0,
                'min': 0,
                'max': 100,
                'step': 0.1,
            },
            'images': {
                'label': 'Images',
                'type': 'image',
                'display': 'output',
            },
        },
    },
}