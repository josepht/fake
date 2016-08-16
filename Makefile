
RPM_WITH_DIRS = rpmbuild --define "_sourcedir ." \
		    --define "_builddir ." \
		    --define "_srcrpmdir ." \
		    --define "_rpmdir ."

srpm:
	$(RPM_WITH_DIRS) -bs fake.spec

rpm:
	$(RPM_WITH_DIRS) -bb fake.spec

sources:
	@echo no sources
