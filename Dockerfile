FROM tensorflow/serving:2.12.1

ENV MODEL_BASE_PATH /models
ENV MODEL_NAME brain_tumor_validator

COPY .models/MRI_validator /models/brain_tumor_validator

RUN echo '#!/bin/bash \n\n\
tensorflow_model_server  --rest_api_port=$PORT \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh

ENTRYPOINT []
CMD ["/usr/bin/tf_serving_entrypoint.sh"]
