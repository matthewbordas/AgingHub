import logging

#pylint: disable=line-too-long,protected-access
def test_configure_logger_succeeds(test_app, caplog) -> None:
    caplog.clear()
    root_logger = logging.getLogger()
    root_logger.addHandler(caplog.handler)
    our_custom_handler = root_logger.handlers[0]
    current_log_format = our_custom_handler.formatter._fmt
    template_log_format = '%(asctime)s %(levelname)s %(filename)s %(funcName)s %(lineno)d %(message)s'
    
    root_logger.info('test_configure_logger_succeeds')
    captured_log = caplog.records[0]
    
    assert test_app is not None
    assert our_custom_handler.name == 'console'
    assert current_log_format == template_log_format
    assert captured_log.levelname == 'INFO'
    assert captured_log.message == 'test_configure_logger_succeeds'
